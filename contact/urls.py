from django.urls import path
from .views import ContactMessageCreateView, SubscriberCreateView

urlpatterns = [
    path('api/contact/', ContactMessageCreateView.as_view(), name='contact-create'),
    path('api/subscribe/', SubscriberCreateView.as_view(), name='subscriber-create'),
]
