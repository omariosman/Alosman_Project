from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Product
from .forms import ProductForm, AddTransactionForm


def home(request):
    return render(request, "home.html")


#return all products
@login_required
def all_products(request):
    all_products = Product.objects.filter(active=True)

    context = {
        "all_products": all_products
    }

    return render(request, 'all_products.html', context)

#return one product by id
def product(request, code):
    product = get_object_or_404(Product, code=code)

    context = {
        "product": product
    }

    return render(request, 'product.html', context)



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) #if form.is_valid():
        #new_form = form.save(commit=False)
        #new_form.user = request.user
        form.save()
        return redirect('/products')

    else:
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, "add_product.html", context)


def edit_product(request, code):
    product = get_object_or_404(Product, code=code)
    #The if part is executed after we press submit
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) #if form.is_valid():
        #new_form = form.save(commit=False)
        #new_form.user = request.user
        form.save()
        return redirect('/products')
    #The else part is executed before we press submit
    else:
        form = ProductForm(instance=product)

    context = {
        "form": form,
    }

    return render(request, "edit_product.html", context)



def add_transactions(request):
    return render(request, "transactions.html")


def add_transaction(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/add_transactions')
    else:
        form = AddTransactionForm()
        
    context = {
        "form": form
    }
    return render(request, "add_transaction.html", context)
