#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30th march 2022
@author: sakib ali
"""
from django.urls import re_path as url
from django.urls import path, include
from homePageAPIs.views import UserAllQueryView,SendQueryMsgView

urlpatterns = [
        url(r'^user/all/query', UserAllQueryView.as_view()),
        url(r'^send/msg', SendQueryMsgView.as_view()),
    ]



