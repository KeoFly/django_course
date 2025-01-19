from django.urls import path
from products.views import product_list, show_product

urlpatterns = [
    path('', product_list, name='list'),
    path('<slug:post_slug>/', show_product, name='prod')
]