from django.urls import path

from .views import ListPayMethod, create_payment_type, create_paymethod, delete_payment_type, edit_payment_type


app_name = 'paymethods'

urlpatterns = [
    path('list/', ListPayMethod.as_view(), name='list'),
    path('create/<int:pk>', create_paymethod, name='create'),
    path('pmtype_add/', create_payment_type, name='pmtype_add'),
    path('pmtype_delete', delete_payment_type, name='pmtype_delete'),
    path('pmtype_edit', edit_payment_type, name='pmtype_edit'),
]

