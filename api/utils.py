from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime


def send_branded_email(subject, template_name, context, recipient_list):
    context["year"] = datetime.now().year
    context["subject"] = subject

    html_content = render_to_string(template_name, context)

    email = EmailMultiAlternatives(
        subject,
        "",
        settings.DEFAULT_FROM_EMAIL,
        recipient_list
    )

    email.attach_alternative(html_content, "text/html")
    email.send()
