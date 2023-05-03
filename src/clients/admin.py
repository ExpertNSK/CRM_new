from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'short_name', 'is_active',
    )
    list_editable = (
        'is_active', 
    )
