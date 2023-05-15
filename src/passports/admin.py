from django.contrib import admin

from .models import Passport


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['serial_number', ]
