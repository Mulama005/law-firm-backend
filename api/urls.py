from django.urls import path
from .views import google_verification, contact

urlpatterns = [
    path(
        "google87ffcc77f7e2b586.html",
        google_verification,
        name="google_verification",
    ),
    path("api/contact/", contact, name="contact"),
]
