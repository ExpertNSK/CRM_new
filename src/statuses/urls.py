from django.urls import path

from .views import ListStatusView, create_status, delete_status, edit_status


app_name = 'statuses'

urlpatterns = [
    path('', ListStatusView.as_view(), name='list'),
    path('create/', create_status, name='add'),
    path('delete', delete_status, name='delete'),
    path('edit', edit_status, name='edit'),
]

