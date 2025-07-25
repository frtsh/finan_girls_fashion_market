from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_favorite/<int:product_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('my_favorites/', views.my_favorites, name='my_favorites'),
    path('profile/', views.profile_view, name='profile'),
]
