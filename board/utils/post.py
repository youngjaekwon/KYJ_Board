from collections import defaultdict

from django.db.models import Q

from board.models import PostSimilarity, PostToken


def update_current_post_related_posts(updated_tokens):
    """
    업데이트 된 Token을 가지고 있는 기존의 Post들의 연관게시글을 업데이트
    """
    targets = PostSimilarity.objects.filter(related_tokens__word__in=updated_tokens)

    for post_sim in targets:
        # 연관게시글 사이에 중복된 단어들
        related_tokens = post_sim.related_tokens.filter(is_upper_60_percent=False).all()

        if related_tokens.count() < 2:
            # Token이 업데이트되어 중복 단어가 2개 미만이 되면 관계 삭제
            post_sim.delete()
        else:
            """
            두 Post 사이의 연관도를 점수로 환산

            전체 게시글중 40% 이하에서 등장하는 단어들의 빈도수 합
            """
            similarity = sum(
                [
                    post_token.count
                    for post_token in PostToken.objects.filter(
                        post=post_sim.post, token__in=related_tokens
                    )
                ]
            )

            # similarity score 업데이트
            post_sim.similarity = similarity
            post_sim.save()


def update_related_posts(posts):
    """
    새로 추가된 게시글의 연관게시글 업데이트
    """
    for post in posts:
        # 연관게시글들의 토큰들을 저장하는 dict
        related_posts = defaultdict(dict)
        # 토큰중 하위 40%에서만 등장하는 토큰들
        for token in post.tokens.filter(is_upper_60_percent=False).all():
            # 토큰을 가지고 있는 다른 Post들
            for post_token in PostToken.objects.filter(Q(token=token) & ~Q(post=post)):
                related_posts[post_token.post][token] = post_token.count
        # 중복되는 토큰이 2개 이상인 경우로 필터링
        related_posts = [
            (post, tokens) for post, tokens in related_posts.items() if len(tokens) > 1
        ]
        # Similarity score 계산 후 저장
        for related_post, tokens in related_posts:
            similarity = sum([count for count in tokens.values()])

            PostSimilarity.objects.create(
                post=post, similar_post=related_post, similarity=similarity
            )
