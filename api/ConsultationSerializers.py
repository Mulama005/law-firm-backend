from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Consultation


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
