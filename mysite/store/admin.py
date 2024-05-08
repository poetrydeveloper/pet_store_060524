from django.contrib import admin

from .models import Tool


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description', 'provider', ]
    list_filter = ['provider']
    search_fields = ['name', 'code']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['code']
