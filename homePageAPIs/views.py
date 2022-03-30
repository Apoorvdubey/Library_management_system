#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30th March 2022
@author: sakib ali
"""
from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authAPIs.serializers import CustomerRegistrationSerializer,BannersListSerializer
from authAPIs.serializers import BooksListSerializer,UserSerializer,QueryTypesSerializer
from homePageAPIs.serializers import UserAdminQuerySerializer
from authAPIs.serializers import UserAdminQueriesContentSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import jwt, datetime
from django.contrib.auth.models import update_last_login
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.crypto import get_random_string
import json
from json import dumps
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from random import randint, randrange
import requests
from django.contrib.auth.models import Group,Permission
from django.db import connection
from users.models import Users
from authAPIs.models import Banners,UserDonations
from userAdminQueryManagement.models import QueryTypes,UserAdminQueries,UserAdminQueriesContents
from bookManagement.models import Book,UserBookmarkBook,UserBookReadingStatus
# Create your views here.

class UserAllQueryView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
       try:
          userId = request.user.id
          user_admin_query = UserAdminQueries.objects.filter(userId__id=userId)
          user_admin_query_serializer = UserAdminQuerySerializer(user_admin_query,many=True)
          response = {
            "error": None,
            "response": {
                   "data": {
                        'userAdminQuery' : user_admin_query_serializer.data
                   },
              "message": {
                'success' : True,
                "successCode": 50,
                "statusCode": status.HTTP_200_OK,
                "successMessage": "User all queries fetched successfully"
              }
            }
          }
          status_code = status.HTTP_200_OK
          return Response(response, status=status_code)    
       except Exception as e:
           status_code = status.HTTP_400_BAD_REQUEST
           response =  {
            "error": {
              "errorCode": 51,
              "statusCode": status.HTTP_400_BAD_REQUEST,
              "errorMessage": str(e)
            },
            "response": None
           }
           return Response(response, status=status_code)

class SendQueryMsgView(generics.UpdateAPIView):
    
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
           request_data = JSONParser().parse(request)
           message = request_data['message']
           userAdminQueryId = request_data['userAdminQueryId']
           userId = request.user.id

           check_usr_query_if_exists = UserAdminQueries.objects.filter(pk=userAdminQueryId).first()
           if check_usr_query_if_exists is None:
                  response = {
                   "error": {
                     "errorCode": 52,
                     "statusCode": status.HTTP_400_BAD_REQUEST,
                     "errorMessage": "Invalid userAdminQueryId!"
                   },
                   "response": None
                  }
                  status_code = status.HTTP_400_BAD_REQUEST
                  return Response(response, status=status_code)
           
           sendUsrQuery = UserAdminQueriesContents()
           sendUsrQuery.message = message
           sendUsrQuery.isSentByAdmin = False
           sendUsrQuery.isRead = False
           sendUsrQuery.userAdminQueryId = check_usr_query_if_exists
           sendUsrQuery.createdAt = datetime.datetime.now()
           sendUsrQuery.updatedAt = datetime.datetime.now()
           sendUsrQuery.save()

           response = {
             "error": None,
             "response": {
               "message": {
                 'success' : True,
                 "successCode": 53,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "User query has been sent to admin"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response =  {
             "error": {
               "errorCode": 54,
               "statusCode": status.HTTP_400_BAD_REQUEST,
               "errorMessage": str(e)
             },
             "response": None
            }
        return Response(response, status=status_code)