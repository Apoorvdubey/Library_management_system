#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24th march 2022
@author: sakib ali
"""
from django.conf.urls import url
from authAPIs.views import UserRegistrationView,UserLoginView
from authAPIs.views import SendEmailOTPView,VerifyEmailOTPView
from authAPIs.views import ChangePasswordView,ForgotPasswordView
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,)
from django.urls import path, include

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^register', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
    url(r'^send/email/otp', SendEmailOTPView.as_view()),
    url(r'^verify/email/otp', VerifyEmailOTPView.as_view()),
    url(r'^change/password', ChangePasswordView.as_view()),
    url(r'^forgot/password', ForgotPasswordView.as_view()),
    ]



