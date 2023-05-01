from django.urls import path

from .views import *


app_name = 'clients'

urlpatterns = [
    path('list/', ListClientView.as_view(), name='list'),
]
