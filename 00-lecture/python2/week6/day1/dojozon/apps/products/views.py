from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')

  context = {
    'purchasable_products': Product.objects.exclude(creator=req.session['user_id']),
    'sellable_products': Product.objects.filter(creator=req.session['user_id']),
  }
  return render(req, 'products/index.html', context)

def new(req):
  return render(req, 'products/new.html')

def show(req):
  pass

def edit(req):
  pass

def create(req):
  errors = Product.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('products:new')
  # create the product if there are no errors
  Product.objects.create_product(req.POST, req.session['user_id'])
  return redirect('products:index')

def update(req):
  pass

def delete(req):
  pass