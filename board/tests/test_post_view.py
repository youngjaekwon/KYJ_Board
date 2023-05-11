from django.test import TestCase, Client

from board.models import Post
from board.factories import PostFactory


class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        PostFactory를 이용하여 Post를 10개 생성
        """
        PostFactory.create_batch(10)

    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        """
        Post의 list를 요청하여 10개가 맞는지 확인
        endpoint: /board/post/
        method: GET
        """
        response = self.client.get("/board/post/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 10)

    def test_post_create(self):
        """
        Post 생성 확인
        endpoint: /board/post/
        method: POST
        """
        post_data = {"title": "Test Title", "content": "Test Content"}
        response = self.client.post("/board/post/", post_data)
        self.assertEqual(response.status_code, 201)
        post = response.json()
        self.assertEqual(post["title"], "Test Title")
        self.assertEqual(post["content"], "Test Content")

    def test_post_retrieve(self):
        """
        Post Retrieve 확인
        endpoint: /board/post/<pk>/
        method: GET
        """
        post_id = 1
        response = self.client.get(f"/board/post/{post_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], post_id)

    def test_post_update(self):
        """
        Post Update 확인
        endpoint: /board/post/<pk>/
        method: PATCH
        """
        post_id = 1
        new_content = "New Test Content"
        data = {"content": new_content}
        response = self.client.patch(
            f"/board/post/{post_id}/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["content"], new_content)

    def test_post_delete(self):
        """
        Post Delete 확인
        endpoint: /board/post/<pk>/
        method: DELETE
        """
        post_id = 1
        response = self.client.delete(f"/board/post/{post_id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 9)
        self.assertFalse(Post.objects.filter(pk=post_id).exists())
