from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from models import *

# Create your views here.
def index(request):
    if 'cart_id' not in request.session:
        cart = Cart(name='empty cart')
        cart.save()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=request.session['cart_id'])
    products = Product.objects.all()
    prod_count = CartProducts.objects.filter(cart__id=cart.id).aggregate(Sum('quantity'))
    context = {'products': products, 'prod_count': prod_count}
    return render(request, 'cart/index.html', context)

def add(request):
    cart = Cart.objects.get(id=request.session['cart_id'])
    product = Product.objects.get(id=request.POST['product_id'])
    cart_prod = CartProducts(cart=cart, product=product, quantity=request.POST['qnty'])
    cart_prod.save()
    messages.add_message(request, messages.INFO, 'Product added to your cart!')
    return redirect('/')

def checkout(request):
    cart = Cart.objects.get(id=request.session['cart_id'])
    temp_list = CartProducts.objects.filter(cart__id=cart.id).values_list('product', 'quantity')
    prod_list = []
    total = 0
    for item in temp_list:
        prod = Product.objects.get(id=item[0])
        prod_list.append({'info': prod, 'qnty': item[1]})
        total += (prod.price * item[1])
    context = {'products': prod_list, 'total': total}
    return render(request, 'cart/checkout.html', context)

def delete(request, product_id):
    cart = Cart.objects.get(id=request.session['cart_id'])
    CartProducts.objects.filter(cart__id=cart.id).filter(product__id=product_id).delete()
    messages.add_message(request, messages.INFO, 'Product removed from your cart!')
    return redirect('/checkout')

def order(request):
    cart = Cart.objects.get(id=request.session['cart_id'])
    cart.name = request.POST['name']
    cart.address = request.POST['address']
    cart.save()
    temp_list = CartProducts.objects.filter(cart__id=cart.id).values_list('product', 'quantity')
    prod_list = []
    total = 0
    for item in temp_list:
        prod = Product.objects.get(id=item[0])
        prod_list.append({'info': prod, 'qnty': item[1]})
        total += (prod.price * item[1])
    context = {'products': prod_list, 'total': total, 'name': cart.name, 'address': cart.address}
    return render(request, 'cart/success.html', context)
