#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30th march 2022
@author: sakib ali
"""
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from users.models import Users
from authAPIs.models import Banners
from bookManagement.models import Book
from userAdminQueryManagement.models import QueryTypes,UserAdminQueries,UserAdminQueriesContents
from authAPIs.serializers import QueryTypesSerializer

class UserAdminQuerySerializer(serializers.ModelSerializer):
    queryTypeId = QueryTypesSerializer()
    class Meta:
        model=UserAdminQueries
        fields = ('userAdminQueryId','queryStatus','createdAt','email','name','queryTypeId')