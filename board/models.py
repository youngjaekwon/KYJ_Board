from django.db import models


class Token(models.Model):
    word = models.CharField(max_length=200)
    is_upper_60_percent = models.BooleanField(default=False)


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    tokens = models.ManyToManyField(Token, through="PostToken")
    related_posts = models.ManyToManyField("self", blank=True, through="PostSimilarity")
    update_needed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostToken(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class PostSimilarity(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    similar_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="similar_post"
    )
    related_tokens = models.ManyToManyField(Token, blank=True)
    similarity = models.IntegerField(default=0)
