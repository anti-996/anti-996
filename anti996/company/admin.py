from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'ctype', 'desc')
    list_display = ('id', 'name', 'ctype', 'desc')
    ordering = ['id']


admin.site.register(Company, CompanyAdmin)
