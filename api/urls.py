from django.urls import path
from .views import google_verification, ContactView

urlpatterns = [
    path(
        "google87ffcc77f7e2b586.html",
        google_verification,
        name="google_verification",
    ),
    path(
        "api/contact/",
        ContactView.as_view(),  # 👈 CBV must use .as_view()
        name="contact",
    ),
]
