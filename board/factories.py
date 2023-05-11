import factory
from faker import Faker

from .models import Post

fake = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: fake.sentence())
    content = factory.LazyAttribute(lambda _: fake.text())
