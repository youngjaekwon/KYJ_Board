from django.test import TestCase

from board.factories import PostFactory
from board.models import Post, Token
from board.tasks import update_post_tokens
from board.utils.token import update_tokens_is_upper_60_percent


class UpdateTokensTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Contet1이라는 단어를 6개의 Post에, Content2라는 단어를 4개의 Post에서 생성
        """
        PostFactory.create_batch(6, content="Test Content1")
        PostFactory.create_batch(4, content="Test Content2")

    def test_token_is_upper_60_percent(self):
        # Token을 생성
        update_post_tokens()

        # Token의 상태를 update
        update_tokens_is_upper_60_percent()

        # 전체 게시글 중 60% 이상에서 등장하는 단어
        self.assertTrue(Token.objects.get(word="Test").is_upper_60_percent)
        self.assertTrue(Token.objects.get(word="Content1").is_upper_60_percent)

        # 전체 게시글 중 40% 이하에서 등장하는 단어
        self.assertFalse(Token.objects.get(word="Content2").is_upper_60_percent)
