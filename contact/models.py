from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)  # <-- Added field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


# New model for subscribers
class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # make sure no duplicates
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
