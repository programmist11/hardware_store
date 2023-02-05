from django.conf import settings
from django.core.mail import send_mail


def send_massage(phone, name):

    send_mail("Позвонить",
              f"{phone} {name}",
              settings.EMAIL_HOST_USER,
              [settings.EMAIL_TO],
              fail_silently=True
              )
    return True

