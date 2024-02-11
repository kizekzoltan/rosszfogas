"""
    Forgalomvezérlő a hirdetés oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render
from .forms import HirdetesForm

# - Views
def shop_view(request):
    return render(request, "shop/hirdetesek.html")


def product_view(request, product_name: str):
    return render(request, "shop/hirdetes.html")


def create_product_view(request):
    form = HirdetesForm()
    return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})


def payment_view(request):
    return render(request, "shop/fizetes.html")