"""
    Forgalomvezérlő a statikus oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render

# - Views
def shop(request):
    context = {}
    return render(request, 'default/shop.html', context)

def kosar(request):
    context = {}
    return render(request, 'default/kosar.html', context)

def checkout(request):
    context = {}
    return render(request, 'default/checkout.html', context)