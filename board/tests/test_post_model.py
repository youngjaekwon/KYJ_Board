from django.test import TestCase

from board.models import Post
from board.factories import PostFactory


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        PostFactory를 이용하여 Post를 10개 생성
        """
        PostFactory.create_batch(10)

    def test_post_count(self):
        """
        생성된 Post가 10개가 맞는지 확인
        """
        self.assertEqual(Post.objects.count(), 10)

    def test_post_creation(self):
        """
        1. Post를 생성후 전체 Post 갯수가 11개가 되는지 확인
        2. Post중 가장 마지막 Instance가 생성한 Post와 동일한지 확인
        """
        Post.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(Post.objects.count(), 11)
        self.assertEqual(Post.objects.last().title, "Test Title")

    def test_post_retrieval(self):
        """
        Post중 하나를 선택 후, 선택된 Post와 Post의 pk로 검색된 Post가 동일한지 확인
        """
        post = Post.objects.first()
        self.assertEqual(post.title, Post.objects.get(pk=post.pk).title)
