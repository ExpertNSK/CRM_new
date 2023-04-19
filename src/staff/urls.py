from django.contrib import admin
from django.urls import path

from staff.views import *


app_name = 'staff'

urlpatterns = [
    path('list/', CustomUserListView.as_view(), name='list'),
    path('detail/<int:pk>/', CustomUserDetailView.as_view(), name='detail'),
]
