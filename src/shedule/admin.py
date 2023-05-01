from django.contrib import admin

from .models import WorkShedule


@admin.register(WorkShedule)
class WorkSheduleAdmin(admin.ModelAdmin):
    list_display = [
        'day'
    ]