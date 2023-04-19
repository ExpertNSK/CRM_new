from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        SignUp.as_view(),
        name='signup',
    ),
    path(
        'login/',
        login_view,
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logout.html'
        ),
        name='logout'
    ),
    path(
        'profile/<int:pk>/',
        EditProfileView.as_view(),
        name='edit'
    )

]
