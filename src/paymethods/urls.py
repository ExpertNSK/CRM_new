from django.urls import path

from .views import ListPayMethod, create_paymethod


app_name = 'paymethods'

urlpatterns = [
    path('list/', ListPayMethod.as_view(), name='list'),
    path('create/<int:pk>', create_paymethod, name='create'),
]

