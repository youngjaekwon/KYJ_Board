from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    related_posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "related_posts", "created_at"]
