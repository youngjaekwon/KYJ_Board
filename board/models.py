from django.db import models


class Token(models.Model):
    """
    Post의 content에서 등장하는 모든 단어들을 Token화한 Model
    Token이 전체게시글 중 60% 이상에서 발견되는지를 is_upper_60_percent에 저장
    """

    word = models.CharField(max_length=200)
    is_upper_60_percent = models.BooleanField(default=False)


class Post(models.Model):
    """
    게시글을 저장하는 Model
    """

    title = models.TextField()
    content = models.TextField()
    tokens = models.ManyToManyField("Token", through="PostToken")
    related_posts = models.ManyToManyField("self", blank=True, through="PostSimilarity")
    update_needed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostToken(models.Model):
    """
    Post와 Token을 연결하는 모델
    Post 안에서 해당 Token이 몇 번 등장하는지 count를 이용해서 저장
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    token = models.ForeignKey("Token", on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class PostSimilarity(models.Model):
    """
    Post와 유사한 Post를 저장
    동시에 등장하는 Token들을 related_tokens에 저장
    Token의 빈도수의 총합을 이용하여 similarity score를 저장
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    similar_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="similar_post"
    )
    related_tokens = models.ManyToManyField("Token", blank=True)
    similarity = models.IntegerField(default=0)
