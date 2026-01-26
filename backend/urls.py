from django.contrib import admin
from django.urls import path
from .views import google_verification, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('google87ffcc77f7e2b586.html', google_verification),
    path('api/contact/', contact),
]
