from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # TODO: save to DB or send email

        return JsonResponse({"success": True, "message": "Consultation submitted"})

    return JsonResponse({"error": "Invalid request"}, status=400)
