from django.db import models

from utils.models import AuditMixin


class Category(models.Model, AuditMixin):
    name = models.CharField(max_length=255)


class Article(models.Model, AuditMixin):
    DELETED = -1
    DRAFT = 0
    PUBLISHED = 1
    REJECTED = 2

    STATUS = (
        (DELETED, "deleted"),
        (DRAFT, "draft"),
        (PUBLISHED, "published"),
        (REJECTED, "rejected"),
    )
    name = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=2048)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.fields.CharField(max_length=1024)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS)

