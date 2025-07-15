from django.shortcuts import render
from .models import Product, ShopImage

def product_list(request):
    products = Product.objects.all()
    shop_images = ShopImage.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'shop_images': shop_images})

