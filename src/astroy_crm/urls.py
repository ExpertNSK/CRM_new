from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from orders.views import OrdersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrdersListView.as_view()),
    path('orders/', include('orders.urls', namespace='orders')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('loaders/', include('loaders.urls', namespace='loaders')),
    path('passports/', include('passports.urls', namespace='passports')),
    path('paymethods/', include('paymethods.urls', namespace='paymethods')),
    path('shedule/', include('shedule.urls', namespace='shedule')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
