from django.db import models
from django.forms import IntegerField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('prod', kwargs={'post_slug': self.slug})
