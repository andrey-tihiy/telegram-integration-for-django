from django.db import models

from apps.service.models import UUIDModel


class UserProfile(UUIDModel):
    telegram_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
