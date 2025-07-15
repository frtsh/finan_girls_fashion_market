from django.contrib import admin
from .models import BlogPost, BlogComment

# Register your models here. 

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_trend', 'is_announcement')
    list_filter = ('is_trend', 'is_announcement', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment)



