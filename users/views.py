from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('product_list')


from products.models import Product
from .models import Favorite
from django.contrib.auth.decorators import login_required

@login_required
def add_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('product_list')

@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'users/my_favorites.html', {'favorites': favorites})

