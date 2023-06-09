from django.contrib import admin
from .models import Loader

@admin.register(Loader)
class LoaderAdmin(admin.ModelAdmin):
    '''Admin model for Loader'''
    list_display = [
        'user',
        'area',
        'phone',
    ]
    list_display_links = ['user', ]
    list_filter = ['area', 'status']
    fieldsets = (
        (None, {
            'fields': (
                'is_active',
                'first_name',
                'last_name',
                'middle_name',
                'phone',
                'whatsapp',
                'photo',
                'area',
                'specialization',
                'status',
                'referer',
            ),
        }),
    )

    def user(self, obj):
        return obj
