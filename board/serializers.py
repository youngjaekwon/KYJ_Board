from rest_framework import serializers

from .models import Post


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

    related_posts = PostListSerializer(many=True, read_only=True)

    """
    TODO
    related_posts 출력 시 similarity score순서로 정렬
    """

    class Meta:
        model = Post
        fields = ["id", "title", "content", "related_posts", "created_at"]
