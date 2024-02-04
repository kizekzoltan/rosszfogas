"""
    Forgalomvezérlő a statikus oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render
from .models import *

# - Views
def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'default/shop.html', context)

def kosar(request):
    context = {}
    return render(request, 'default/kosar.html', context)

def checkout(request):
    context = {}
    return render(request, 'default/checkout.html', context)