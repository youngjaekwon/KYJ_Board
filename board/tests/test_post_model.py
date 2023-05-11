from django.test import TestCase

from board.models import Post
from board.factories import PostFactory


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostFactory.create_batch(10)

    def test_post_count(self):
        self.assertEqual(Post.objects.count(), 10)

    def test_post_creation(self):
        Post.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(Post.objects.count(), 11)
        self.assertEqual(Post.objects.last().title, "Test Title")

    def test_post_retrieval(self):
        post = Post.objects.first()
        self.assertEqual(post.title, Post.objects.get(pk=post.pk).title)
