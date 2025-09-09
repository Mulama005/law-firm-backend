from rest_framework import generics, status
from rest_framework.response import Response
from .models import ContactMessage, Subscriber
from .serializers import ContactMessageSerializer, SubscriberSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        print("📥 Incoming contact request data:", request.data)  # 👈 Log incoming data
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("❌ Validation errors:", serializer.errors)  # 👈 Log validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        instance = serializer.save()

        # Send notification email to admin
        send_mail(
            subject=f"📩 New Contact Message from {instance.name}",
            message=f"Name: {instance.name}\nEmail: {instance.email}\nMessage:\n{instance.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        # Optional: Auto reply to sender
        send_mail(
            subject="✅ We received your message",
            message=f"Hello {instance.name},\n\nThanks for reaching out. Our team will get back to you soon.\n\nBest regards,\nLaw Website Team",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
        )


@method_decorator(csrf_exempt, name="dispatch")
class SubscriberCreateView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        print("📥 Incoming subscriber data:", request.data)  # 👈 Log incoming data
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("❌ Validation errors:", serializer.errors)  # 👈 Log validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        instance = serializer.save()

        # Send notification email to admin
        send_mail(
            subject="🆕 New Subscriber",
            message=f"A new user subscribed with email: {instance.email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        # Optional: Auto reply
        send_mail(
            subject="🎉 Welcome to our community!",
            message="Thanks for subscribing! You’ll now receive updates from us.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
        )
