from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from lawyers.views import LawyerViewSet
from services.views import ServiceViewSet
from contact.views import ContactMessageCreateView, SubscriberCreateView

router = routers.DefaultRouter()
router.register(r'lawyers', LawyerViewSet)
router.register(r'services', ServiceViewSet)
# contact is handled separately below, so remove this:
# router.register(r'contact', ContactMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # only lawyers & services
    path('api/contact/', ContactMessageCreateView.as_view(), name='contact-create'),  # contact form
     path('api/subscribe/', SubscriberCreateView.as_view(), name='subscribe'), 
]
