from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def google_verification(request):
    return HttpResponse(
        "google-site-verification: google87ffcc77f7e2b586.html",
        content_type="text/plain; charset=utf-8"
    )

@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({"success": True})
