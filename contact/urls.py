from django.urls import path
from .views import google_verification

urlpatterns = [
    path(
        "google87ffcc77f7e2b586.html",
        google_verification,
        name="google-verification",
    ),
]
