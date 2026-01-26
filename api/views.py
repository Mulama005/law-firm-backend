from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Consultation
import json

@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Consultation.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            message=data.get("message"),
        )

        return JsonResponse({"success": True})
