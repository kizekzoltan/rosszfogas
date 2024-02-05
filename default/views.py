"""
    Forgalomvezérlő a statikus oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render, get_object_or_404
from .models import *

# - Views
def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'default/shop.html', context)

def kosar(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'default/kosar.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'default/checkout.html', context)

def item_detail(request, item_name):
    product = get_object_or_404(Product, name=item_name)
    return render(request, 'default/item_detail.html', {'product': product})