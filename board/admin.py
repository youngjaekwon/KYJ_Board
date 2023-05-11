from django.contrib import admin

from .models import (
    Post,
    Token,
    PostToken,
    PostSimilarity,
)

models = [
    Post,
    Token,
    PostToken,
    PostSimilarity,
]

admin.site.register(models)
