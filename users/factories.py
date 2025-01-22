import factory
from factory.django import DjangoModelFactory
from news.models import Article
from datetime import datetime

from products.models import Product, Category


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence')
    description = factory.Faker('text', max_nb_chars=199)
    text = factory.Faker('text')
    pub_date = factory.Faker('date_time_between', start_date=datetime.fromisoformat('2024-01-01T00:00:00'))
    status = Article.Status.PUBLISH

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    slug = factory.Faker('word')
    price = factory.Faker('random_int', min=5, max=30)
    category = factory.SubFactory(CategoryFactory)
    stock = factory.Faker('random_int', min=0, max=100)