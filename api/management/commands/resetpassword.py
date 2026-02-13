from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Reset password for an existing superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        username = "admin"
        new_password = "Admin"

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS("Password reset successfully!"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User does not exist."))
