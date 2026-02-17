from django.urls import path
from .views import google_verification, ContactView, SubscribeView

urlpatterns = [
    path(
        "google87ffcc77f7e2b586.html",
        google_verification,
        name="google_verification",
    ),
    path("api/contact/", ContactView.as_view(), name="contact"),
    path("api/subscribe/", SubscribeView.as_view(), name="subscribe"),
]
