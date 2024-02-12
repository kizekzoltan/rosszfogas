from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    ALLAPOT_CHOICES = [
        ('--válasszon--', '--Válasszon--'),
        ('bontatlan', 'Bontatlan'),
        ('újszerű', 'Újszerű'),
        ('használt', 'Használt'),
        ('megviselt', 'Megviselt'),
    ]
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
    allapot = models.CharField(max_length=50, choices=ALLAPOT_CHOICES, default='--válasszon--')
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