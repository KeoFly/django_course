from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    prod_list = Product.objects.all()
    context = dict(prod_list=prod_list)
    return render(request, 'product_list.html', context)

def show_product(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)

    data = {
        'name': post.name,
        'price': post.price,
        'category': post.category,
        'stock': post.stock,
    }
    return render(request, 'product.html', context=data)