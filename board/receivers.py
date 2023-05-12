from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post


@receiver(post_save, sender=Post)
def handle_post_save(sender, instance, **kwargs):
    """
    Post가 업데이트 될 때 Token 및 연관게시글을 업데이트 해야하는 상태로 변경
    """
    instance.update_needed = True
    instance.save()
