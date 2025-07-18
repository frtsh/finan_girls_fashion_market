from django.contrib import admin
from .models import Product, Category, ShopImage, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ShopImage)
admin.site.register(Review)
