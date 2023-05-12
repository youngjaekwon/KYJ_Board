from django.db import transaction

from celery import shared_task
import nltk

from .models import Post, Token, PostToken


@shared_task
@transaction.atomic
def update_post_tokens():
    """
    Post가 create 또는 update 되면 Token을 업데이트 하는 Task

    nltk로 본문을 토큰화 하여 저장
    """

    targets = Post.objects.filter(update_needed=True)
    if not targets:
        return

    # 전체 토큰 갯수 저장
    tokens_count = Token.objects.count()

    for post in targets:
        tokens = nltk.word_tokenize(post.content)

        # 추출된 토큰중에서 특수문자를 제외
        tokens = [token for token in tokens if len(token) > 1 or token.isalpha()]

        # Post에 속해있는 모든 Token들을 삭제
        PostToken.objects.filter(post=post).delete()

        # 새로 추가된 Token들을 저장
        freq_dist = nltk.FreqDist(tokens)
        for word, freq in freq_dist.items():
            token, _ = Token.objects.get_or_create(word=word)
            PostToken.objects.create(post=post, token=token, count=freq)

    if tokens_count != Token.objects.count():
        """
        TODO
        모든 Post의 Token 등록 후 전체 Token의 변경사항이 있으면
        Token들의 is_upper_60_percent(전체 게시글중 60%에서 등장하는지)를 업데이트 해야함
        """
        pass

    """
    TODO
    Post에 연관게시글 리스트를 업데이트 해야함
    """
