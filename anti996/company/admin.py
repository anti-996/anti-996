from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    ordering = ['id']


admin.site.register(Company, CompanyAdmin)
