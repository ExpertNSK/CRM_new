from django.urls import path

from .views import ListPayMethod, create_payment_type, create_paymethod


app_name = 'paymethods'

urlpatterns = [
    path('list/', ListPayMethod.as_view(), name='list'),
    path('create/<int:pk>', create_paymethod, name='create'),
    path('pmtype_add/', create_payment_type, name='pmtype_add'),
]

