from django.contrib import admin
from django.urls import path, include, re_path
from .api import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('register', RegisterAPI.as_view(), name="register"),
    path('user/me', MeUserApi.as_view(), name='meUser'),
    path('user/orders', AllOrderUser.as_view(), name='orders'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]