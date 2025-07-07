from django.db import models
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

