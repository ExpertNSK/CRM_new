from django.urls import path

from .views import ListSpecView, create_specializations, delete_specializations, edit_specializations


app_name = 'specs'

urlpatterns = [
    path('list', ListSpecView.as_view(), name='list'),
    path('create/', create_specializations, name='add'),
    path('delete/', delete_specializations, name='delete'),
    path('edit/', edit_specializations, name='edit')
]

