from django.db import transaction

from celery import shared_task
import nltk

from .models import Post, Token, PostToken
from .utils.token import update_tokens_is_upper_60_percent
from .utils.post import update_current_post_related_posts, update_related_posts


@shared_task
@transaction.atomic
def update_post_task():
    """
    Post가 create 또는 update 되면 Token 및 연관게시글을 업데이트
    """

    targets = Post.objects.filter(update_needed=True)
    if not targets:
        return

    # 전체 토큰 갯수 저장
    tokens_count = Token.objects.count()

    for post in targets:
        # nltk로 본문을 토큰화
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
        # 토큰의 상태를 업데이트하고 업데이트된 토큰들을 가져옴
        updated_tokens = update_tokens_is_upper_60_percent()
        # 업데이트된 토큰들을 가지고 있는 게시글들의 연관게시글을 업데이트
        update_current_post_related_posts(updated_tokens)

    # 새로 추가된 게시글들의 연관게시글을 업데이트
    update_related_posts(targets)
