"""
    Forgalomvezérlő a fiók oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm


# - Views
def profile_view(request):
    return render(request, "account/fiok.html")

def register_view(request):
    form = RegistrationForm()
    return render(request, 'account/regisztracio.html', {'form': form})

def login_view(request):
    form = LoginForm()
    return render(request, 'account/bejelentkezes.html', {'form':form})