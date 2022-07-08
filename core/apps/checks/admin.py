from django.contrib import admin

from core.apps.checks.models import Check


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'type')
    list_filter = ('status', 'type', 'printer')
