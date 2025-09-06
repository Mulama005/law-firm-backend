# lawyers/admin.py
from django.contrib import admin
from .models import Lawyer

@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "email")  # adjust fields
    search_fields = ("name", "specialization")
    list_filter = ("specialization",)
    ordering = ("name",)
