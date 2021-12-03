from django.contrib import messages
from django.db import models
from accounts.models import User
# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider')
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    category_choice=(
        ('Fruits','Fruits'),
        ('Vagetable','Vagetable'),
        ('Oil','Oil'),
        ('Rice','Rice'),
        ('Others','Others'),
    )
    category = models.CharField(max_length=60,choices=category_choice,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    quantity = models.CharField(max_length=100,blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='seller')
    mobile = models.CharField(max_length=15,blank=True,null=True)
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.mobile
    
    class Meta:
        ordering = ('-timestamp',)
        verbose_name='Bid'
        verbose_name_plural='Bids'
        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100,null=True,blank=True)
    messages= models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name