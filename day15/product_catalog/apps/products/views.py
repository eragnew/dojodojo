from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from models import Product

# Create your views here.
def homepage(request):
    return redirect('/products')

def index(request):
    products = Product.objects.all()
    manufacturers = Product.objects.values_list('manufacturer', flat=True).distinct()
    context = {'products': products, 'manufacturers': manufacturers}
    return render(request, 'products/index.html', context)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    manufacturers = Product.objects.values_list('manufacturer', flat=True).distinct()
    context = {'product': product, 'manufacturers': manufacturers}
    return render(request, 'products/product.html', context)

def update(request, product_id):
    if request.method != 'POST':
        raise Http404('Invalid HTTP method!')
    go_back = False
    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.INFO, 'Product Name cannot be blank!')
        go_back = True
    elif len(request.POST['name']) < 8:
        messages.add_message(request, messages.INFO, 'Product Name must be at least 8 characters!')
        go_back = True
    if len(request.POST['price']) < 1:
        messages.add_message(request, messages.INFO, 'Price cannot be blank!')
        go_back = True
    elif float(request.POST['price']) < 0:
        messages.add_message(request, messages.INFO, 'Price cannot be less than $0!')
        go_back = True
    if len(request.POST['description']) < 1:
        messages.add_message(request, messages.INFO, 'Description cannot be blank!')
        go_back = True
    elif len(request.POST['description']) > 50:
        messages.add_message(request, messages.INFO, 'Description cannot be more than 50 characters!')
        go_back = True
    if go_back:
        return redirect('/products/' + str(product_id))
    else:
        prod = Product.objects.get(id=product_id)
        prod.name = request.POST['name']
        prod.manufacturer = request.POST['manufacturer']
        prod.price = float(request.POST['price'])
        prod.description = request.POST['description']
        prod.save()
        return redirect('/products')

def delete(request, product_id):
    if request.method != 'POST':
        raise Http404('Invalid HTTP method!')
    prod = Product.objects.get(id=product_id)
    prod.delete()
    return redirect('/products')

def create(request):
    if request.method != 'POST':
        raise Http404('Invalid HTTP method!')
    go_back = False
    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.INFO, 'Product Name cannot be blank!')
        go_back = True
    elif len(request.POST['name']) < 8:
        messages.add_message(request, messages.INFO, 'Product Name must be at least 8 characters!')
        go_back = True
    if len(request.POST['price']) < 1:
        messages.add_message(request, messages.INFO, 'Price cannot be blank!')
        go_back = True
    elif float(request.POST['price']) < 0:
        messages.add_message(request, messages.INFO, 'Price cannot be less than $0!')
        go_back = True
    if len(request.POST['description']) < 1:
        messages.add_message(request, messages.INFO, 'Description cannot be blank!')
        go_back = True
    elif len(request.POST['description']) > 50:
        messages.add_message(request, messages.INFO, 'Description cannot be more than 50 characters!')
        go_back = True
    if go_back:
        return redirect('/products')
    else:
        prod = Product(name=request.POST['name'], manufacturer=request.POST['manufacturer'], price=float(request.POST['price']), description=request.POST['description'])
        prod.save()
        return redirect('/products')
