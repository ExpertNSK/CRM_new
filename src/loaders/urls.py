from django.urls import path

from loaders.views import *


app_name = 'loaders'

urlpatterns = [
    path('list/', ListLoaderView.as_view(), name='list'),
    path('create/', CreateLoaderView.as_view(), name='create'),
    path('detail/<int:pk>', DetailLoaderView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateLoaderView.as_view(), name='update'),
    path('spec_add/', CreateSpecializationView.as_view(), name='spec_add'),
    path('spec_list/', ListSpecializationView.as_view(), name='spec_list'),
    path('spec_edit/<int:pk>/', EditSpecializationView.as_view(), name='spec_edit'),
    path('spec_delete/<int:pk>/', DeleteSpecializationView.as_view(), name='spec_delete'),
    path('status_add/', CreateStatusView.as_view(), name='status_add'),
    path('status_list/', ListStatusView.as_view(), name='status_list'),
    path('status_edit/<int:pk>/', EditStatusView.as_view(), name='status_edit'),
    path('status_delete/<int:pk>/', DeleteStatusView.as_view(), name='status_delete'),
]
