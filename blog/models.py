from django.db import models
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_trend = models.BooleanField(default=False, help_text='Mark as a latest trend post')
    is_announcement = models.BooleanField(default=False, help_text='Mark as a shop news/announcement')

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

