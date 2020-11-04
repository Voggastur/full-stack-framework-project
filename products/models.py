from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='noimage.png')

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A model of Reviews, linked to Product and User """
    reviewed_product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="product_reviews")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    header = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.header
