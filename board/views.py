from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, PostListSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.order_by("-created_at")
    serializer_class = {"default": PostSerializer, "list": PostListSerializer}
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """
        request의 action에 따라 serializer 선택
        """
        return self.serializer_class.get(self.action, self.serializer_class["default"])
