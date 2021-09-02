from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/products.html', context)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
