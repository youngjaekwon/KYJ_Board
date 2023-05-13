from django.test import TestCase

from board.models import Post
from board.receivers import handle_post_save


class PostUpdateReceiverTest(TestCase):
    """
    board/receivers 의 handle_post_save에 대한 테스트
    """

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title="Test Title", content="Test Content", update_needed=False
        )

    def test_update_needed(self):
        """
        Post가 업데이트되면 updated_needed가 True로 변경되는지 확인
        """
        post = Post.objects.first()
        self.assertFalse(post.update_needed)

        post.content = "New Test Content"
        post.save()

        post.refresh_from_db()
        self.assertTrue(post.update_needed)
