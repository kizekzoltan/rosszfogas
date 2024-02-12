"""
    Forgalomvezérlő a hirdetés oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render
from .forms import HirdetesForm
from default.models import *
from django.shortcuts import redirect

# - Views
def shop_view(request):
    return render(request, "shop/hirdetesek.html")


def product_view(request, product_name: str):
    return render(request, "shop/hirdetes.html")

def hirdetes_letrehozasa(request):
    if request.method == 'POST':
        form = HirdetesForm(request.POST, request.FILES)
        if form.is_valid():
            
            product = Product(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                feladocim = form.cleaned_data['feladocim'],
                feladoorszag = form.cleaned_data['feladoorszag'],
                kategoria = form.cleaned_data['kategoria'],
                allapot = form.cleaned_data['allapot'],
                customer=request.user.customer
            )
            product.save()
            return redirect('fiok') 
    else:
        form = HirdetesForm()
    return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})

def payment_view(request):
    return render(request, "shop/fizetes.html")