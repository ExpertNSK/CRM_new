from django.urls import path
from .views import *


app_name = 'shedule'

urlpatterns = [
    path('', shedule_view, name='shedule'),
    path('calling', calling, name='calling')
]
