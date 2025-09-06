from rest_framework import viewsets
from .models import Lawyer
from .serializers import LawyerSerializer

class LawyerViewSet(viewsets.ModelViewSet):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

# Create your views here.
