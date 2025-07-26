from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email, user_first_name):
    subject = 'Welcome to Finan Girls Fashion Market!'
    message = f'Thank you {user_first_name} for joining our website Finan Girls Fashion Market. We are excited to have you!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
