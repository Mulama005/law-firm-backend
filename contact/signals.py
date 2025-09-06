from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Subscriber


@receiver(post_save, sender=ContactMessage)
def notify_admin_on_contact(sender, instance, created, **kwargs):
    if created:
        subject = "📩 New Contact Message"
        message = (
            f"Name: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Phone: {instance.phone}\n"
            f"Company: {instance.company}\n\n"
            f"Message:\n{getattr(instance, 'message', 'No message provided')}"
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])


@receiver(post_save, sender=Subscriber)
def notify_admin_on_subscribe(sender, instance, created, **kwargs):
    if created:
        subject = "🆕 New Subscriber"
        message = f"A new subscriber has joined:\nEmail: {instance.email}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
