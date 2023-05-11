from django.test import TestCase

from board.models import Post, Token, PostSimilarity


class PostSmilarityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Post를 2개, Token을 1개 생성 후 이를 이용해 PostSimilarity 생성
        """
        post1 = Post.objects.create(title="Test Title", content="Test Content")
        post2 = Post.objects.create(title="Test Title", content="Test Content")
        token = Token.objects.create(word="test_word")
        post_similarity = PostSimilarity.objects.create(post=post1, similar_post=post2)
        post_similarity.related_tokens.add(token)
        post_similarity.similarity = 1
        post_similarity.save()

    def test_post_similarity_creation(self):
        """
        PostSimilarity가 올바르게 생성되었는지 확인
        """
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        token = Token.objects.first()
        self.assertEqual(PostSimilarity.objects.count(), 1)
        self.assertEqual(PostSimilarity.objects.last().post, post1)
        self.assertEqual(PostSimilarity.objects.last().similar_post, post2)
        self.assertTrue(
            PostSimilarity.objects.last().related_tokens.filter(pk=token.pk).exists()
        )
        self.assertEqual(PostSimilarity.objects.last().similarity, 1)

    def test_related_posts_m2m_field(self):
        """
        PostSimilarity를 이용한 Post의 ManyToManyField(related_posts) 확인
        """
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        self.assertTrue(post1.related_posts.filter(pk=post2.pk).exists())
