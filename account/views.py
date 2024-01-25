"""
    Forgalomvezérlő a fiók oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render

# - Views
def register_view(request):
    return render(request, "account/regisztracio.html")


def login_view(request):
    return render(request, "account/bejelentkezes.html")


def profile_view(request):
    return render(request, "account/fiok.html")