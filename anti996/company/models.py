from django.db import models


from utils.models import AuditMixin


class Company(models.Model, AuditMixin):
    UNKNOWN = 0
    GOOD = 1
    BAD = 2

    CTYPES = (
        (UNKNOWN, "unknown"),
        (GOOD, "good"),
        (BAD, "bad")
    )
    name = models.CharField(max_length=255)
    ctype = models.IntegerField(choices=CTYPES)
    desc = models.TextField()
