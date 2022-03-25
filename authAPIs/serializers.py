#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24th march 2022
@author: sakib ali
"""
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from users.models import Users

class CustomerRegistrationSerializer(serializers.ModelSerializer):
     
    class Meta:  
        model = Users
        fields = ['fullName','email','mobileNo','password','gender']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = Users.objects.create(
            fullName=validated_data['fullName'],
            mobileNo=validated_data['mobileNo'],
            email=validated_data['email'],       
            password=make_password(validated_data['password']),
            gender=validated_data['gender'],
        )
        return user