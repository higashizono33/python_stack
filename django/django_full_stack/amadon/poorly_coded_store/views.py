from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    request.session['quantity'] = int(request.POST['quantity'])
    request.session['price'] = request.POST['price']
    quantity_from_form = request.session['quantity']
    product = Product.objects.get(id=request.session['price'])
    total_charge = quantity_from_form * product.price
    total_charge = round(total_charge, 2)
    # print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    return redirect('/checkout')

def checkout(request):
    quantity_from_form = request.session['quantity']
    product = Product.objects.get(id=request.session['price'])
    total_charge = quantity_from_form * product.price
    total_charge = round(total_charge, 2)
    combined_quantity = Order.objects.aggregate(Sum('quantity_ordered'))
    combined_total_charge = Order.objects.aggregate(Sum('total_price'))
    context = {
        'price': product.price,
        'quantity': quantity_from_form,
        'total_charge': total_charge,
        **combined_quantity,
        **combined_total_charge,
    }
    return render(request, "store/checkout.html", context)