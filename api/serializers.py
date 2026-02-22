from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Consultation, Subscriber


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"

    def create(self, validated_data):
        consultation = super().create(validated_data)

        
        # CLIENT CONFIRMATION EMAIL
        
        client_context = {
            "name": consultation.name,
        }

        client_html = render_to_string(
            "emails/consultation_email.html",
            client_context
        )

        client_email = EmailMultiAlternatives(
            subject="Consultation Request Received - Eredi Law Advocates",
            body=f"Dear {consultation.name}, we have received your request.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[consultation.email],
        )

        client_email.attach_alternative(client_html, "text/html")
        client_email.send(fail_silently=False)

       
        #ADMIN NOTIFICATION EMAIL
        
        admin_context = {
            "name": consultation.name,
            "email": consultation.email,
            "phone": consultation.phone,
            "message": consultation.message,
        }

        admin_html = render_to_string(
            "emails/admin_consultation_email.html",
            admin_context
        )

        admin_email = EmailMultiAlternatives(
            subject=" New Consultation Request Received",
            body="A new consultation request has been submitted.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],  
        )

        admin_email.attach_alternative(admin_html, "text/html")
        admin_email.send(fail_silently=False)

        return consultation


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"

    def create(self, validated_data):
        subscriber = super().create(validated_data)

        
        subscriber_context = {
            "email": subscriber.email,
        }

        subscriber_html = render_to_string(
            "emails/subscriber_welcome_email.html",
            subscriber_context
        )

        welcome_email = EmailMultiAlternatives(
            subject="Welcome to Eredi Law Newsletter",
            body="Thank you for subscribing to Eredi Law Advocates.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscriber.email],
        )

        welcome_email.attach_alternative(subscriber_html, "text/html")
        welcome_email.send(fail_silently=False)

        
        admin_email = EmailMultiAlternatives(
            subject="New Newsletter Subscriber",
            body=f"New subscriber: {subscriber.email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
        )

        admin_email.send(fail_silently=False)

        return subscriber