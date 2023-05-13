from django.test import TestCase

from board.factories import PostFactory
from board.models import Post, Token
from board.tasks import update_post_task


class UpdateRelatedPostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostFactory.create_batch(
            6, content="이것은 테스트용 본문입니다. 6개의 게시글에서 '사과'라는 단어가 등장합니다."
        )
        PostFactory.create_batch(
            4, content="이것은 테스트용 본문입니다. 4개의 게시글에서 '포도'라는 단어가 등장합니다."
        )

    def test_update_related_posts_for_new_posts(self):
        """
        연관게시글이 잘 적용되는지 확인
        """
        update_post_task()
        apple_posts = Post.objects.order_by("created_at")[:6]
        grape_posts = Post.objects.order_by("created_at")[6:]

        # 전체 게시글중 60%
        self.assertFalse(
            apple_posts[0].related_posts.filter(id=apple_posts[1].id).exists()
        )
        # 전체 게시글중 40%
        self.assertTrue(
            grape_posts[0].related_posts.filter(id=grape_posts[1].id).exists()
        )
