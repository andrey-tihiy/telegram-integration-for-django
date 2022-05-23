import uuid

from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, editable=False, null=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, editable=False, null=True)

    class Meta:
        abstract = True
