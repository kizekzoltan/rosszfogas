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
    current_user = request.user
    customer = Customer.objects.get(user=current_user)
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
                customer=request.user.customer
            )

            if 'image' not in request.FILES:
                form.add_error('image', "Képet kötelező feltölteni!")
                return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})

            if product.price < 1:
                form.add_error('price', "Az ár nem lehet kisebb 1 HUF-nál!")
                return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})

            if product.price > 100000000:
                form.add_error('price', "Az ár nem lehet nagyobb 100.000.000 HUF-nál!")
                return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})

            extension = product.image.name.split('.')[-1].lower()
            if extension == 'gif':
                form.add_error('image', "Nem tölthetsz fel gif-et Söli!")
                return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form})

            else:
                product.save()
                return redirect('fiok')
    else:
        form = HirdetesForm()
    return render(request, 'shop/hirdetes_letrehozasa.html', {'form': form, 'customer': customer})

def payment_view(request):
    return render(request, "shop/fizetes.html")