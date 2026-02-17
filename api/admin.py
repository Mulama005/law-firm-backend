from django.contrib import admin
from .models import Consultation
from .models import Subscriber

admin.site.register(Consultation)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)