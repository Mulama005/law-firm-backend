from django.contrib import admin
from .models import ContactMessage, Subscriber


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company", "service", "created_at")
    search_fields = ("name", "email", "phone", "company", "service")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
