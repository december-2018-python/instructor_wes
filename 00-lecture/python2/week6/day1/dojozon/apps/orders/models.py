from django.db import models
from ..users.models import User
from ..products.models import Product

# Create your models here.
class OrderManager(models.Manager):
  pass

class Order(models.Model):
  is_fulfilled = models.BooleanField()
  user = models.ForeignKey(User, related_name="orders")
  products = models.ManyToManyField(Product, related_name="orders")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)