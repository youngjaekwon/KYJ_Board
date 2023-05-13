from rest_framework import serializers

from .models import Post, PostSimilarity


class PostListSerializer(serializers.ModelSerializer):
    """
    Post의 List용 Serializer
    """

    class Meta:
        model = Post
        fields = ["id", "title", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    """
    Post의 Retrieve용 Serializer
    """

    # related_posts = PostListSerializer(many=True, read_only=True)

    related_posts = serializers.SerializerMethodField()

    def get_related_posts(self, instance):
        """
        연관게시글을 연관도 순서로 정렬
        """
        related_posts = instance.related_posts.order_by("-similar_post")
        return PostListSerializer(related_posts, many=True).data

    class Meta:
        model = Post
        fields = ["id", "title", "content", "related_posts", "created_at"]
