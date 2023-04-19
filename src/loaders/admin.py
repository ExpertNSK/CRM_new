from django.contrib import admin
from .models import Loader, Passport, PayMethod

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

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['serial_number', ]


@admin.register(PayMethod)
class PayMethodAdmin(admin.ModelAdmin):
    list_display = ['pay_method', ]
