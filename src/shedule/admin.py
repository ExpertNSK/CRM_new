from django.contrib import admin

from .models import CallResult, WorkShedule


@admin.register(WorkShedule)
class WorkSheduleAdmin(admin.ModelAdmin):
    list_display = [
        'day'
    ]

@admin.register(CallResult)
class CallResult(admin.ModelAdmin):
    list_display = [
        'loader'
    ]