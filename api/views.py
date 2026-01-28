from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
            print("ERRORS:", serializer.errors)  # 👈 ADD THIS
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(
            {"message": "Consultation submitted successfully"},
            status=status.HTTP_201_CREATED
        )
