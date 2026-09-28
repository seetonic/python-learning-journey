from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "inventory/product_list.html", {"products":products})