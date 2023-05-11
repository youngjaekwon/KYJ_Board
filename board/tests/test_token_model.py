from django.test import TestCase

from board.models import Token
from board.factories import TokenFactory


class TokenModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        TokenFactory를 이용하여 Token을 10개 생성
        """
        TokenFactory.create_batch(10)

    def test_token_count(self):
        """
        생성된 Token이 10개가 맞는지 확인
        """
        self.assertEqual(Token.objects.count(), 10)

    def test_token_is_not_upper_60_percent_creation(self):
        """
        전중 게시글 중 60% 이상에서 발견되지 않는 Token을 생성
        (is_upper_60_percent field의 default 값을 이용하는 방법과, 명시적으로 값을 주는 방법 두 가지를 테스트)
        1. Token 생성 후 전체 Token 갯수가 11개가 되는지 확인
        2. Token 중 가장 마지막 Instance가 생성한 Token과 동일한지 확인
        3. 생성된 Token의 is_upper_60_percent field가 False인지 확인
        4. is_upper_60_percnet field에 명시적으로 값을 전달 후 확인
        """
        # is_upper_60_percent의 default값을 이용
        Token.objects.create(word="test_word")
        self.assertEqual(Token.objects.count(), 11)
        self.assertEqual(Token.objects.last().word, "test_word")
        self.assertFalse(Token.objects.last().is_upper_60_percent)

        # 명시적으로 False 값을 전달
        Token.objects.create(word="test_is_upper_60_false", is_upper_60_percent=False)
        self.assertFalse(Token.objects.last().is_upper_60_percent)

    def test_token_is_upper_60_percent_creation(self):
        """
        전체 게시글 중 60% 이상에서 발견되는 Token을 생성후 확인
        """
        Token.objects.create(word="test_is_upper_60_true", is_upper_60_percent=True)
        self.assertTrue(Token.objects.last().is_upper_60_percent)

    def test_token_retrieval(self):
        """
        Token중 하나를 선택 후, 선택된 Token과 Token의 pk로 검색된 Token이 동일한지 확인
        """
        token = Token.objects.filter()
        self.assertEqual(token.word, Token.objects.get(pk=token.pk).word)
