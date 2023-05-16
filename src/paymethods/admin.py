from django.contrib import admin

from .models import PaymentType, PayMethod


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('payment_type', )


@admin.register(PayMethod)
class PayMethodAdmin(admin.ModelAdmin):
    list_display = ('payment_type', )
