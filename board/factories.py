import factory
from faker import Faker

from .models import Post, Token

fake = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: fake.sentence())
    content = factory.LazyAttribute(lambda _: fake.text())


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    word = factory.LazyAttribute(lambda _: fake.word())
