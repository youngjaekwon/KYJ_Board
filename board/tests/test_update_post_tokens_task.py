from django.test import TestCase

from board.models import Post, Token, PostToken
from board.factories import PostFactory
from board.tasks import update_post_tokens


class UpdatePostTokensTaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostFactory.create_batch(10)

    def test_task_work(self):
        """
        update_post_tokens task가 작동하는지 확인

        1. 임의의 Post를 불러와 연관된 Token이 없는지 확인
        2. task 실행
        3. Token이 잘 적용되었는지 확인
        """
        post = Post.objects.first()
        self.assertFalse(PostToken.objects.filter(post=post).exists())

        update_post_tokens()

        self.assertTrue(PostToken.objects.filter(post=post).exists())

    def test_token_in_post_content(self):
        """
        update_post_tokens task가 생성한 Token이 Post의 content에 있는지 확인
        """
        update_post_tokens()

        token = Token.objects.first()
        post = PostToken.objects.filter(token=token).first().post

        self.assertTrue(token.word in post.content)
