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
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list')
        else:
            error = 'Invalid credentials. Please try again.'
    return render(request, 'users/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('product_list')


from products.models import Product
from .models import Favorite, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'biography', 'social_link']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'social_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://your-social-link.com'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get('current_password')
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 or p2:
            if not current:
                raise forms.ValidationError('You must enter your current password to change your password.')
            if self.user and not self.user.check_password(current):
                raise forms.ValidationError('Current password is incorrect.')
            if p1 != p2:
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

@login_required
def profile_view(request):
    user = request.user
    profile = user.profile
    favorites = Favorite.objects.filter(user=user)
    tab = request.GET.get('tab', 'profile')
    if request.method == 'POST':
        tab = request.POST.get('tab', 'profile')
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        password_form = PasswordChangeForm(request.POST, user=user)
        if tab == 'profile':
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('profile')
        elif tab == 'privacy':
            if password_form.is_valid():
                if password_form.cleaned_data['password1']:
                    user.set_password(password_form.cleaned_data['password1'])
                    user.save()
                return redirect('profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
        password_form = PasswordChangeForm(user=user)
    return render(request, 'users/profile.html', {
        'user': user,
        'profile': profile,
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
        'favorites': favorites,
        'tab': tab,
    })

@login_required
def add_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('product_list')

@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'users/my_favorites.html', {'favorites': favorites})

