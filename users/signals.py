from django.db.models.signals import post_save, post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)

@receiver(post_migrate)
def ensure_all_users_have_profile(sender, **kwargs):
    for user in User.objects.all():
        UserProfile.objects.get_or_create(user=user) 