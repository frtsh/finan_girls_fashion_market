from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from cloudinary.models import CloudinaryField

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # avoid duplicate favorites

    def __str__(self):
        return f"{self.user.username} favorited {self.product.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    biography = models.TextField(blank=True)
    social_link = models.URLField(blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"Profile of {self.user.username}"

