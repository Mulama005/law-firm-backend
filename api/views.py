from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Consultation
import json


def google_verification(request):
    return HttpResponse(
        "google-site-verification: google87ffcc77f7e2b586.html",
        content_type="text/plain"
    )


@csrf_exempt
def contact(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            Consultation.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                message=data.get("message"),
            )

            return JsonResponse({"success": True}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
