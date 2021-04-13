from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product, Manufacturer
from .forms import ProductForm

class Products(View):
    template = 'home.html'

    def get(self, request):
        products = Product.objects.all()
        form = ProductForm()
        context = {
            'form': form,
            'products': products, 
        }
        return render(request, self.template, context)
    def post(self, request):
        products = Product.objects.all()
        form = ProductForm(request.POST)
        context = {
            'form': form,
            'products': products, 
        }
        if form.is_valid():
            form.save()
            return redirect('products')
        return render(request, self.template, context)

class EditProduct(View):
    template = 'edit.html'
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductForm(initial={
            'manufacturer': product.manufacturer,
            'name': product.name,
            'price': product.price,
            'description': product.description,
        })
        context = {
            'form': form,
            'product': product, 
        }
        return render(request, self.template, context)
    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST, instance=product)
        context = {
            'form': form,
            'product': product, 
        }
        if form.is_valid():
            form.save()
            return redirect('editing', id=id)
        return render(request, self.template, context)

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')