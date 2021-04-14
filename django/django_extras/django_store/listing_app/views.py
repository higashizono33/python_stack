from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product, Manufacturer
from .forms import ProductForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.template.loader import render_to_string
from django.http import HttpResponse
# from django.template import RequestContext
import json


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
        resp = {}
        if form.is_valid():
            form.save()
            resp['success'] = True
            rendered_page = render_to_string(self.template, context=context, request=request) 
            resp['page'] = rendered_page
            # return redirect('products')
        else:
            resp['success'] = False
            csrf_context = {}
            csrf_context.update(csrf(request))
            productForm_html = render_crispy_form(form, context=csrf_context)
            resp['html'] = productForm_html
        
        return HttpResponse(json.dumps(resp), content_type='application/json')

        # return render(request, self.template, context)

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
    products = Product.objects.all()
    form = ProductForm()
    context = {
        'form': form,
        'products': products, 
    }
    resp = {}
    rendered_table = render_to_string('table_partial.html', context=context, request=request) 
    resp['table'] = rendered_table
    return HttpResponse(json.dumps(resp), content_type='application/json')
    
    # return redirect('products')