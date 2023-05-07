from django.urls import path

from .views import *


app_name='orders'

urlpatterns = [
    path('list/', OrdersListView.as_view(), name='list'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='detail')
]