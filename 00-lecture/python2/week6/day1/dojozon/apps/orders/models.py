from django.db import models
from ..users.models import User
from ..products.models import Product

# Create your models here.
class OrderManager(models.Manager):
  def add_product(self, form_data, user_id):
    cart = self.get_active_cart(user_id)
    product = Product.objects.get(id=form_data['product_id'])
    cart.products.add(product)
    cart.save()
    product.num_available = product.num_available - 1
    product.save()
    return
  
  def get_active_cart(self, user_id):
    active_orders = self.filter(user=user_id).filter(in_progress=False)
    if active_orders:
      cart = active_orders[0]
    else:
      cart = self.create_default_order(user_id)
    return cart
  
  def create_default_order(self, user_id):
    user = User.objects.get(id=user_id)
    return self.create(
      is_fulfilled = False,
      in_progress = False,
      user = user,
    )

class Order(models.Model):
  is_fulfilled = models.BooleanField()
  in_progress = models.BooleanField()
  user = models.ForeignKey(User, related_name="orders")
  products = models.ManyToManyField(Product, related_name="orders")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = OrderManager()