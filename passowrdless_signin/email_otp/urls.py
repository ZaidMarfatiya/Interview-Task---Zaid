from django.urls import path
from .views import *


urlpatterns = [
    path('reqister/', RegisterView.as_view(), name='register'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('verify-otp/', OTPVerifyView.as_view(), name='verify-otp'),
    path('userinfo/', UserInfo.as_view(), name='userinfo'),
]