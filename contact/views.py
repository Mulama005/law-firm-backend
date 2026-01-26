from django.http import HttpResponse

def google_verification(request):
    return HttpResponse(
        "google-site-verification: google87ffcc77f7e2b586.html",
        content_type="text/plain"
    )
