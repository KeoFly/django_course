from news.models import Article
from products.models import Product


def get_main_news(min_date='2024-01-01'):
   return Article.objects.filter(
        status=Article.Status.PUBLISH,
        pub_date__date__gte=min_date
    ).order_by('-pub_date', )[0]

def get_news_list(exclude_news):
    return Article.objects.filter(
        status=Article.Status.PUBLISH
    ).exclude(pk__in=[article.pk for article in exclude_news])

def get_products_list():
    return Product.objects.all()