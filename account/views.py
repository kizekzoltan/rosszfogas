"""
    Forgalomvezérlő a fiók oldalakhoz
    @package rosszfogas
"""
from default.models import Customer, Product
from django.db import IntegrityError
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def profile_view(request):
    current_user = request.user
    customer = Customer.objects.get(user=current_user)
    products = Product.objects.filter(customer=customer)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('fiok')
    else:
        form = UserProfileForm(instance=customer)
        print(form.errors)

    return render(request, "account/fiok.html", {'customer': customer, 'products': products, 'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            terms_agreed = form.cleaned_data['terms_checkbox']
            
            if password != password_confirm:
                form.add_error('password_confirm', "A jelszavak nem egyeznek!")
                return render(request, 'account/regisztracio.html', {'form': form})

            if not terms_agreed:
                form.add_error('terms_checkbox', "Kérjük fogadd el a felhasználói feltételeket!")
                return render(request, 'account/regisztracio.html', {'form': form})

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                customer = Customer.objects.create(user=user, name=username, email=email)
                login(request, user)

            except IntegrityError:
                form.add_error('username', "Ezzel a felhasználóval már regisztráltak.")
                return render(request, 'account/regisztracio.html', {'form': form})
            
            return redirect('shop')
    else:
        form = RegistrationForm()
        
    return render(request, 'account/regisztracio.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop')
    else:
        form = LoginForm()
    return render(request, 'account/bejelentkezes.html', {'form': form})

@login_required(redirect_field_name=None)
def logout_view(request):
    logout(request)
    return redirect(reverse('bejelentkezes'))

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('fiok')
    return redirect('fiok')


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    try:
        user = User.objects.get(id=customer.user_id)
    except ObjectDoesNotExist:
        return HttpResponse("Error: User not found", status=404)
    
    if request.method == 'POST':
        user.delete()
        customer.delete()
        return redirect('regisztracio') 
    return redirect('fiok')