from django.shortcuts import render, redirect
from .models import Order

# Create your views here.
def index(req):
  return render(req, 'orders/index.html')

def cart(req):
  context = {
    'cart': Order.objects.filter(user=req.session['user_id']).filter(in_progress=False)[0]
  }
  return render(req, 'orders/cart.html', context)

def add_product(req):
  Order.objects.add_product(req.POST, req.session['user_id'])
  return redirect('products:index')
