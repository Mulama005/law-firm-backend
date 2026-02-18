from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.conf import settings

from .models import Subscriber
from .serializers import SubscriberSerializer, ConsultationSerializer
from .utils import send_branded_email


#Google Site Verification
def google_verification(request):
    return HttpResponse(
        "google-site-verification: google87ffcc77f7e2b586.html",
        content_type="text/plain",
    )


#Consultation View
class ContactView(APIView):
    def post(self, request):
        serializer = ConsultationSerializer(data=request.data)

        if not serializer.is_valid():
            print("ERRORS:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        consultation = serializer.save()

        #Send confirmation email to client
        send_branded_email(
            subject="Consultation Request Received - Eredi Law Advocates",
            template_name="emails/consultation_email.html",
            context={
                "name": consultation.name,
            },
            recipient_list=[consultation.email],
        )

        #Notify admin
        send_branded_email(
            subject="New Consultation Request",
            template_name="emails/consultation_email.html",
            context={
                "name": consultation.name,
            },
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        return Response(
            {"message": "Consultation submitted successfully"},
            status=status.HTTP_201_CREATED
        )


#Subscribe View
class SubscribeView(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        subscriber = serializer.save()

        #Send confirmation email to subscriber
        send_branded_email(
            subject="Welcome to Eredi Law Advocates",
            template_name="emails/subscription_email.html",
            context={},
            recipient_list=[subscriber.email],
        )

        #Notify admin of new subscriber
        send_branded_email(
            subject="New Subscriber Alert",
            template_name="emails/subscription_email.html",
            context={},
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        return Response(
            {"message": "Subscription successful!"},
            status=status.HTTP_201_CREATED
        )
