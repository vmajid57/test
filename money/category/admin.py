from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("source", "price", "publish", "created_at")
    search_fields = ("source", "price", "created_at")
    list_filter = ("source", "price", "created_at")
    ordering = ['source', 'created_at']
# Register your models here.
admin.site.register(Category, CategoryAdmin)

