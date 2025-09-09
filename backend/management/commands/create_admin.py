# backend/management/commands/create_admin.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create a default admin user"

    def handle(self, *args, **kwargs):
        username = "admin"
        email = "admin@example.com"
        password = "AdminPassword123"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser created: {username} / {password}"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin user already exists."))
