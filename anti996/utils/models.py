
from django.db import models
from django.contrib.auth.models import User


class AuditMixin:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    updater = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
