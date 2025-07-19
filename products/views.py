from django.shortcuts import render
from .models import Product, ShopImage, Review, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django.http import HttpResponse
from django.core.management import call_command

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

def product_list(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    products = Product.objects.all()
    if search_query:
        products = products.filter(name__icontains=search_query)  # You can also add description__icontains=search_query if desired
    if category_id:
        products = products.filter(category_id=category_id)
    shop_images = ShopImage.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'shop_images': shop_images,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    else:
        user_review = None
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm(instance=user_review)
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'user_review': user_review,
    })


def load_fixtures(request):
    try:
        call_command('loaddata', 'products.json')
        call_command('loaddata', 'shopimages.json')
        return HttpResponse('Fixtures loaded!')
    except Exception as e:
        return HttpResponse(f'Error: {e}', status=500)

