from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # manufacturer = forms.CharField()

    class Meta:
        model = Product
        fields = ['manufacturer', 'name', 'price', 'description']
