from django import forms
from django.forms import fields
from .models import Product

class ProductForm(forms.ModelForm):
        class Meta:
            model=Product
            fields=[
                "category",
                "name",
                "price",
                "image",
                "description",
                "quantity"
            ]
    # category = forms.CharField(required=True , widget=forms.TextInput)
    # name = forms.CharField(required=True , widget=forms.TextInput)
    # price = forms.DecimalField(required=True , widget=forms.NumberInput)
    # image = forms.ImageField(required=True,widget=forms.Image)