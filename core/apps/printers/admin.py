from django.contrib import admin

from core.apps.printers.models import Printer


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key', 'check_type')
