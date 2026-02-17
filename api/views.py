from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber
from .serializers import SubscriberSerializer
from .serializers import ConsultationSerializer


def google_verification(request):
    return HttpResponse(
        "google-site-verification: google87ffcc77f7e2b586.html",
        content_type="text/plain",
    )


class ContactView(APIView):
    def post(self, request):
        serializer = ConsultationSerializer(data=request.data)

        if not serializer.is_valid():
            print("ERRORS:", serializer.errors)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(
            {"message": "Consultation submitted successfully"},
            status=status.HTTP_201_CREATED
        )

class SubscribeView(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Subscription successful!"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
