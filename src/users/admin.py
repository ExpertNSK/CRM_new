from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'email',
        'phone',
        'role',
    ]
    list_display_links = ['user']
    list_filter = ['role']
    fieldsets = (
        (None, {
            'fields': (
                'last_name', 'first_name',
                'middle_name', 'phone',
                'email', 'password', 'role',
            ),
        }),
    )
    
    def user(self, obj):
        return obj
    
    def save_model(self, request, obj, form, change):
        if CustomUser.objects.filter(phone=obj.phone).exists():
            user = CustomUser.objects.filter(phone=obj.phone).get()
            if user.password != obj.password:
                obj.password = make_password(obj.password)
        else:
            obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)