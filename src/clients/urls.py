from django.urls import path

from .views import *


app_name = 'clients'

urlpatterns = [
    path('list/', ListClientView.as_view(), name='list'),
    path('create/', CreateClientView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailClientView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteClientView.as_view(), name='delete')
]
