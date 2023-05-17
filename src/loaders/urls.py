from django.urls import path

from loaders.views import *


app_name = 'loaders'

urlpatterns = [
    path('list/', ListLoaderView.as_view(), name='list'),
    path('create/', CreateLoaderView.as_view(), name='create'),
    path('detail/<int:pk>', DetailLoaderView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateLoaderView.as_view(), name='update'),
]
