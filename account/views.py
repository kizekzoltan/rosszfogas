"""
    Forgalomvezérlő a fiók oldalakhoz
    @package rosszfogas
"""
from default.models import Customer, Product, Topic, Comment
from django.db import IntegrityError
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, UserProfileForm, CommentForm, TopicForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.db.models import Count
from .utils import send_registration_confirmation_email
import os


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
                send_registration_confirmation_email(email)
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
        if product.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(product.image))
            if os.path.exists(image_path):
                os.remove(image_path)
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

def forum_cucc(request):
    topics = Topic.objects.annotate(num_comments=Count('comment'))
    current_user = request.user
    customer = Customer.objects.get(user=current_user)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.creator = request.user
            topic.save()
            return redirect('forumcucc')
    else:
        form = TopicForm()
    return render(request, 'account/topic_list.html', {'topics': topics, 'form': form, 'customer': customer, 'current_user': current_user})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = Comment.objects.filter(topic=topic)
    num_comments = comments.count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.commenter = request.user
            comment.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = CommentForm()
    return render(request, 'account/topic_detail.html', {'topic': topic, 'comments': comments, 'form': form, 'num_comments': num_comments})


def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('forumcucc')
    return redirect('forumcucc')


def send_order(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.sent = True
        product.save()
        
        return redirect('fiok')