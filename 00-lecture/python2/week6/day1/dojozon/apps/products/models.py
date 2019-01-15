from django.db import models
from ..users.models import User

# Create your models here.
class ProductManager(models.Manager):
  pass

class Product(models.Model):
  name = models.CharField(max_length=255)
  num_available = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  creator = models.ForeignKey(User, related_name="products")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)