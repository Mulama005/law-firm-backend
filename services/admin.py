# services/admin.py
from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")  # adjust fields
    search_fields = ("title", "description")
    list_filter = ("price",)
    ordering = ("title",)
