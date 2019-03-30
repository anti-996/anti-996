from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    ordering = ['id']


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['id']


admin.site.register(Article, ArticleAdmin)


admin.site.register(Category, CategoryAdmin)
