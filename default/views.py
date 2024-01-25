"""
    Forgalomvezérlő a statikus oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render

# - Views
def index_view(request):
    return render(request, "default/fooldal.html")


def about_us_view(request):
    return render(request, "default/rolunk.html")


def forum_view(request):
    return render(request, "default/forum.html")