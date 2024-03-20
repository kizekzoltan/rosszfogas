"""
    Forgalomvezérlő a statikus oldalakhoz
    @package rosszfogas
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth import logout
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from account.utils import send_order_confirmation_email
from django.shortcuts import render
from django.db.models import Q



def shop(request):
    if request.user.is_authenticated:
        current_user = request.user
        customer = get_object_or_404(Customer, user=current_user)
    else:
        customer = None

    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'customer': customer, 'myFilter': myFilter}

    return render(request, 'default/shop.html', context)

    context = {'items':items, 'order':order}
    return render(request, 'default/checkout.html', context)

def item_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'default/item_detail.html', {'product': product})

def updateItem(request):
    return JsonResponse('Item was added', safe=False)

def gyik(request):
    return render(request, 'default/gyik.html')


def order(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user.customer
    context = {
        'product': product,
        'customer': customer,
    }
    return render(request, 'default/order.html', context)

def place_order(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.orderer_name = request.POST.get('orderer_name')
        product.orderer_phone = request.POST.get('orderer_phone')
        product.orderer_location = request.POST.get('orderer_location')
        product.orderer_email = request.POST.get('orderer_email')
        product.ordered = True
        product.save()
        send_order_confirmation_email(product)
        return redirect('orders')

def orders(request):
    orderer_name = request.user.customer.name
    orders = Product.objects.filter(orderer_name=orderer_name)
    context = {
        'orders': orders
    }
    return render(request, 'default/orders.html', context)


def rolunk(request):
    return render(request, 'default/rolunk.html')


def received_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        if product.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(product.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        product.delete()
        return redirect('orders')
    return redirect('orders')

def korlatok(request):
    if not request.user.is_superuser:
        return redirect('shop')
    customers = Customer.objects.all()
    return render(request, 'default/korlatok.html', {'customers': customers})

def search_users(request):
    search_query = request.GET.get('search')
    if search_query:
        customers = Customer.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
    else:
        customers = Customer.objects.all()
    return render(request, 'default/korlatok.html', {'customers': customers})


def ban(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        ban_type = request.POST.get('ban_type')
        customer = Customer.objects.get(pk=customer_id)

        if ban_type == 'sale':
            customer.banned_ad = True
            customer.save()
        elif ban_type == 'forum':
            customer.banned_forum = True
            customer.save()
        elif ban_type == 'unsale':
            customer.banned_ad = False
            customer.save()
        elif ban_type == 'unforum':
            customer.banned_forum = False
            customer.save()
    return redirect('korlatok')
