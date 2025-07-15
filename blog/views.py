from django.shortcuts import render
from .models import BlogPost, BlogComment
from django.shortcuts import redirect

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    trends = posts.filter(is_trend=True)
    announcements = posts.filter(is_announcement=True)
    comments = BlogComment.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        if name and comment_text:
            BlogComment.objects.create(name=name, comment=comment_text, post=posts.first() if posts else None)
        return redirect('blog_list')

    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'trends': trends,
        'announcements': announcements,
        'comments': comments,
    })

