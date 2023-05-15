from django.urls import path

from .views import ajax_edit, create_passport

app_name = 'passports'

urlpatterns = [
    path('create/<int:pk>/', create_passport, name='create'),
    path('edit/', ajax_edit, name='edit')
]
