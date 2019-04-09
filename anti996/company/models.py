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
    name = models.CharField(verbose_name="名称", max_length=255)
    ctype = models.IntegerField(verbose_name="类型", choices=CTYPES)
    homepage = models.URLField(verbose_name="主页链接", null=True, blank=True)
    evidence = models.ImageField(verbose_name="证据", null=True, blank=True)
    desc = models.TextField(verbose_name="简介", null=True, blank=True)

    class Meta:
        ordering = ['-id']
