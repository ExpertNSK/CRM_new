from django.urls import path

from .views import ListPaymentType


app_name = 'paymethods'

urlpatterns = [
    path('list', ListPaymentType.as_view(), name='list'),
]

