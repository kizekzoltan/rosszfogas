from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.urls import reverse
#

from django.db.models.signals import pre_delete
import os
from django.conf import settings


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True , default="")
    lastname = models.CharField(max_length=200, null=True , default="")
    location = models.CharField(max_length=200, null=True, default="")
    phone = models.CharField(
        max_length=12,
        null=True,
        default="",
        validators=[
            RegexValidator(
                regex=r'^[\d()+-]*$',
                message='A telefonszám csak számokat, illetve + karaktert tartalmazhat',
                code='ervenytelen_szam'
            )
        ]
    )


    def __str__(self):
        return self.name


class Product(models.Model):
    KATEGORIA_CHOICES = [
        ('--válasszon--', '--Válasszon--'),
        ('autó', 'Autó'),
        ('élelmiszer', 'Élelmiszer'),
        ('egyéb', 'Egyéb'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    description = models.TextField()
    feladocim = models.CharField(max_length=100, null=True, blank=True)
    feladoorszag = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='default/images/')
    kategoria = models.CharField(max_length=50, choices=KATEGORIA_CHOICES, default='--válasszon--')
    terms_checkbox = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        if self.image:
            return '/images/' + str(self.image)
        return ''



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    cim = models.CharField(max_length=200, null=True)
    varos = models.CharField(max_length=200, null=True)
    orszag = models.CharField(max_length=200, null=True)
    iranyitoszam = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



class Topic(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_detail', args=[str(self.id)])

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.topic.title}"
