from django.test import TestCase, Client
import factory

from news.models import Article
from users.factories import ArticleFactory, ProductFactory
from users.services import get_main_news, get_products_list
from .models import Category, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')

class SimpleViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Sample category'

class CategoryFactoryTest(TestCase):
    def test_factory_creation(self):
        """
        Case: Тест названия категории.
        Expected: Получить Sample category.
        """
        category = CategoryFactory.create()
        self.assertEqual(category.name, 'Sample category')

class TestMainNews(TestCase):

    def test_main_news_with_min_date(self):
        expected_article = ArticleFactory.create()
        unexpected_articles = ArticleFactory.create_batch(5, pub_date='2023-01-01')
        article = get_main_news(min_date='2023-01-01')

        self.assertEqual(article, expected_article)

class ProductCategoryTest(TestCase):
    def test_product_category_creation(self):
        product = ProductFactory.create()
        prod = get_products_list()[0]

        self.assertIsNotNone(product.category)
        self.assertTrue(len(prod.category.name) > 0)
        self.assertTrue(str(prod.category_id).isdigit())
        self.assertTrue(str(prod.stock).isdigit())
        self.assertTrue(str(int(prod.price)).isdigit())
        self.assertTrue(len(prod.slug) > 0)
