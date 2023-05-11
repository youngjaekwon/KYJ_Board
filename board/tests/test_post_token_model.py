from django.test import TestCase

from board.models import Post, Token, PostToken


class PostTokenTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Post, Token을 각각 생성후 이를 이용해 PostToken 생성
        """
        post = Post.objects.create(title="Test Title", content="Test Content")
        token = Token.objects.create(word="test_word")
        PostToken.objects.create(post=post, token=token, count=1)

    def test_post_token_creation(self):
        """
        PostToken이 올바르게 생성되었는지 확인
        """
        post = Post.objects.first()
        token = Token.objects.first()
        self.assertEqual(PostToken.objects.count(), 1)
        self.assertEqual(PostToken.objects.last().post, post)
        self.assertEqual(PostToken.objects.last().token, token)
        self.assertEqual(PostToken.objects.last().count, 1)

    def test_tokens_m2m_field(self):
        """
        PostToken Model을 이용한 Post의 ManyToManyField(tokens) 확인
        """
        post = Post.objects.first()
        token = Token.objects.first()
        self.assertTrue(post.tokens.filter(pk=token.pk).exists())
