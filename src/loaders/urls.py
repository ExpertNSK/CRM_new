from django.urls import path

from loaders.views import *


app_name = 'loaders'

urlpatterns = [
    path('list/', ListLoaderView.as_view(), name='list'),
    path('create/', CreateLoaderView.as_view(), name='create'),
    path('detail/<int:pk>', DetailUpdateLoaderViewSet.as_view(), name='detail'),
    path('detail/passport_add/<int:pk>', CreatePassportView.as_view(), name='passport_add'),
    path('detail/passport_edit/<int:pk>', UpdatePassportView.as_view(), name='passport_edit'),
    path('detail/pay_method_add/<int:pk>', CreatePayMethodView.as_view(), name='pay_method_fl_add'),
    path('detail/pay_method_edit/<int:pk>', UpdatePayMethodView.as_view(), name='pay_method_fl_edit'),
    path('spec_add/', CreateSpecializationView.as_view(), name='spec_add'),
    path('spec_list/', ListSpecializationView.as_view(), name='spec_list'),
    path('spec_edit/<int:pk>/', EditSpecializationView.as_view(), name='spec_edit'),
    path('spec_delete/<int:pk>/', DeleteSpecializationView.as_view(), name='spec_delete'),
    path('status_add/', CreateStatusView.as_view(), name='status_add'),
    path('status_list/', ListStatusView.as_view(), name='status_list'),
    path('status_edit/<int:pk>/', EditStatusView.as_view(), name='status_edit'),
    path('status_delete/<int:pk>/', DeleteStatusView.as_view(), name='status_delete'),
    path('pay_method_add/', CreatePayMethodListView.as_view(), name='pay_method_add'),
    path('pay_method_list/', ListPayMethodListView.as_view(), name='pay_method_list'),
    path('pay_method_edit/<int:pk>/', EditPayMethodListView.as_view(), name='pay_method_edit'),
    path('pay_method_delete/<int:pk>/', DeletePayMethodListView.as_view(), name='pay_method_delete'),
]
