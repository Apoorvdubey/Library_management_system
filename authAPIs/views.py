#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24th March 2022
@author: sakib ali
"""
from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authAPIs.serializers import CustomerRegistrationSerializer,BannersListSerializer
from authAPIs.serializers import BooksListSerializer,UserSerializer
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
from authAPIs.models import Banners
from bookManagement.models import Book
# Create your views here.

class UserRegistrationView(CreateAPIView):

    customer_serializer_class = CustomerRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
       try:
           request_data = JSONParser().parse(request)
           json_request = json.dumps(request_data)
           dictionary = json.loads(json_request)
           mobileNo = request_data['mobileNo']
           email = request_data['email']

           check_mobile_no_if_exists = Users.objects.filter(mobileNo=mobileNo).first()
           if check_mobile_no_if_exists is not None:
                response = {
                 "error": {
                   "errorCode": 1,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "mobileNo already exists!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

           check_email_if_exists = Users.objects.filter(email=email).first()
           if check_email_if_exists is not None:
                response = {
                 "error": {
                   "errorCode": 2,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "email already exists!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

           serializer = self.customer_serializer_class(data=request_data)
           if serializer.is_valid(raise_exception=True):
                serializer.save()   
                user = Users.objects.filter(mobileNo=mobileNo).first()  
                if user is not None:
                   userId = user.id
                   fullName = user.fullName
                   mobileNo = user.mobileNo
                   email = user.email
                   gender = user.gender

                refresh = RefreshToken.for_user(user)
                response = {
                  "error": None,
                  "response": {
                     "data": {
                          'userId' : userId,
                          'fullName' : fullName,
                          'mobileNo' : mobileNo,
                          'email' : email,
                          'gender' : gender,
                          'refresh' : str(refresh),
                          'jwtToken' : str(refresh.access_token),
                     },
                    "message": {
                      'success' : True,
                      "successCode": 3,
                      "statusCode": status.HTTP_200_OK,
                      "successMessage": "User registered successfully"
                    }
                  }
                }
                status_code = status.HTTP_200_OK
                return Response(response, status=status_code)

           response = {
            "error": {
              "errorCode": 4,
              "statusCode": status.HTTP_200_OK,
              "errorMessage": "failed to register user"
            },
            "response": None
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code)
       except Exception as e:
           status_code = status.HTTP_400_BAD_REQUEST
           response =  {
            "error": {
              "errorCode": 5,
              "statusCode": status.HTTP_400_BAD_REQUEST,
              "errorMessage": str(e)
            },
            "response": None
           }
           return Response(response, status=status_code) 

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            firstLoginId = Q(email=email)
            user = Users.objects.filter(firstLoginId).first()  
            if user is not None:
               userId = user.id
               fullName = user.fullName
               mobileNo = user.mobileNo
               email = user.email
          
            if user is None:
                response = {
                 "error": {
                   "errorCode": 6,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "User not found!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

            if not user.check_password(password):
                response = {
                 "error": {
                   "errorCode": 7,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "Incorrect password!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

            if user.isDeleted==1:
                response = {
                 "error": {
                   "errorCode": 8,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "Your account has been removed by the admin!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

            if user.isActive==0:
                response = {
                 "error": {
                   "errorCode": 9,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "Your account has been deactivated by the admin.Please contact admin for support!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)
            
            refresh = RefreshToken.for_user(user)
            response = {  
              "error": None,
              "response": {
                     "data": {
                          'userId' : userId,
                          'fullName' : fullName,
                          'mobileNo' : mobileNo,
                          'email' : email,
                          'refresh' : str(refresh),
                          'jwtToken' : str(refresh.access_token),
                     },
                "message": {
                  'success' : True,
                  "successCode": 10,
                  "statusCode": status.HTTP_200_OK,
                  "successMessage": "User logged in successfully"
                }
              }
            }
            update_last_login(None, user)
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)    

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response =  {
             "error": {
               "errorCode": 11,
               "statusCode": status.HTTP_400_BAD_REQUEST,
               "errorMessage": str(e)
             },
             "response": None
            }
            return Response(response, status=status_code)

class SendEmailOTPView(generics.UpdateAPIView):

    permission_classes = (AllowAny,)
    def post(self, request):
       try:  
           email = request.data['email']
           user = Users.objects.filter(email=email).first()  
           if user is not None:
              fullName = user.fullName
           
           if user is None:
               response = {
                "error": {
                  "errorCode": 6,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "User not found!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)
          
           generate_otp = get_random_string(length=6)
           Users.objects.filter(email=email).update(otp=generate_otp)
           send_mail(   
                 'EBook Reader',
                 'Confirm your email address',
                 'alisakib899@gmail.com',
                 [email],
                 fail_silently=False,
                 html_message = render_to_string('mail/verify_mail.html', {'generate_otp': generate_otp, 'fullName': fullName})
           )
           response = {
             "error": None,
             "response": {
              "data": {
                    'email' : email
               },
               "message": {
                 'success' : True,
                 "successCode": 12,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "Mail sent successfully"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code) 
       except Exception as e:
          status_code = status.HTTP_400_BAD_REQUEST
          response =  {
           "error": {
             "errorCode": 13,
             "statusCode": status.HTTP_400_BAD_REQUEST,
             "errorMessage": str(e)
           },
           "response": None
          }
          return Response(response, status=status_code) 

class VerifyEmailOTPView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    def post(self, request):
       try:  
           otp_request = request.data['otp']
           user = Users.objects.filter(otp=otp_request).first()  
           if user is not None:                 
              fullName = user.fullName                  
              otp = user.otp
           if user is None or otp_request!=otp:
               response = {
                "error": {
                  "errorCode": 14,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "Invalid OTP!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)

           response = {
             "error": None,
             "response": {
               "message": {
                 'success' : True,
                 "successCode": 15,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "OTP matched successfully"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code) 
       except Exception as e:
          status_code = status.HTTP_400_BAD_REQUEST
          response =  {
           "error": {
             "errorCode": 16,
             "statusCode": status.HTTP_400_BAD_REQUEST,
             "errorMessage": str(e)
           },
           "response": None
          }
          return Response(response, status=status_code) 

class ChangePasswordView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    def post(self, request):
       try:  
           userId = request.user.id
           oldPassword = request.data['oldPassword']
           newPassword = request.data['newPassword']
           confirmPassword = request.data['confirmPassword']
           user = Users.objects.filter(pk=userId).first()  
           if user is not None:             
              fullName = user.fullName                  
              otp = user.otp
              email = user.email
           
           if user is None:
               response = {
                "error": {
                  "errorCode": 6,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "User not found!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)

           if newPassword!=confirmPassword:
               response = {
                "error": {
                  "errorCode": 19,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "newPassword and confirmPassword did not matched!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)

           if not user.check_password(oldPassword):
                response = {
                 "error": {
                   "errorCode": 7,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "Incorrect password!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)
         
           Users.objects.filter(pk=userId).update(password=make_password(newPassword))
           send_mail(   
                 'EBook Reader',
                 'Password Changed Successfully',
                 'alisakib899@gmail.com',
                 [email],
                 fail_silently=False,
                 html_message = render_to_string('mail/password_changed.html', {'fullName': fullName,'newPassword': newPassword})
           )
           response = {
             "error": None,
             "response": {
               "message": {
                 'success' : True,
                 "successCode": 17,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "Password changed successfully"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code) 
       except Exception as e:
          status_code = status.HTTP_400_BAD_REQUEST
          response =  {
           "error": {
             "errorCode": 18,
             "statusCode": status.HTTP_400_BAD_REQUEST,
             "errorMessage": str(e)
           },
           "response": None
          }
          return Response(response, status=status_code) 

class ForgotPasswordView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    def post(self, request):
       try:  
           otp_request = request.data['otp']
           newPassword = request.data['newPassword']
           confirmPassword = request.data['confirmPassword']
           user = Users.objects.filter(otp=otp_request).first()  
           if user is not None:             
              fullName = user.fullName                  
              otp = user.otp
              email = user.email
           
           if user is None or otp_request!=otp:
               response = {
                "error": {
                  "errorCode": 14,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "Invalid OTP!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)

           if newPassword!=confirmPassword:
               response = {
                "error": {
                  "errorCode": 19,
                  "statusCode": status.HTTP_400_BAD_REQUEST,
                  "errorMessage": "newPassword and confirmPassword did not matched!"
                },
                "response": None
               }
               status_code = status.HTTP_400_BAD_REQUEST
               return Response(response, status=status_code)
         
           Users.objects.filter(otp=otp).update(password=make_password(newPassword))
           send_mail(   
                 'EBook Reader',
                 'Password Changed Successfully',
                 'alisakib899@gmail.com',
                 [email],
                 fail_silently=False,
                 html_message = render_to_string('mail/password_changed.html', {'fullName': fullName,'newPassword': newPassword})
           )
           response = {
             "error": None,
             "response": {
               "message": {
                 'success' : True,
                 "successCode": 17,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "Password changed successfully"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code) 
       except Exception as e:
          status_code = status.HTTP_400_BAD_REQUEST
          response =  {
           "error": {
             "errorCode": 18,
             "statusCode": status.HTTP_400_BAD_REQUEST,
             "errorMessage": str(e)
           },
           "response": None
          }
          return Response(response, status=status_code)

class BannersView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
       try:
          banners = Banners.objects.all()
          banners_serializer = BannersListSerializer(banners,many=True)
          response = {
            "error": None,
            "response": {
                   "data": {
                        'banners' : banners_serializer.data
                   },
              "message": {
                'success' : True,
                "successCode": 21,
                "statusCode": status.HTTP_200_OK,
                "successMessage": "Banners fetched successfully"
              }
            }
          }
          status_code = status.HTTP_200_OK
          return Response(response, status=status_code)    
       except Exception as e:
           status_code = status.HTTP_400_BAD_REQUEST
           response =  {
            "error": {
              "errorCode": 22,
              "statusCode": status.HTTP_400_BAD_REQUEST,
              "errorMessage": str(e)
            },
            "response": None
           }
           return Response(response, status=status_code)   

class BooksListView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
       try:
          books = Book.objects.all()
          books_serializer = BooksListSerializer(books,many=True)
          response = {
            "error": None,
            "response": {
                   "data": {
                        'booksList' : books_serializer.data
                   },
              "message": {
                'success' : True,
                "successCode": 23,
                "statusCode": status.HTTP_200_OK,
                "successMessage": "Books fetched successfully"
              }
            }
          }
          status_code = status.HTTP_200_OK
          return Response(response, status=status_code)    
       except Exception as e:
           status_code = status.HTTP_400_BAD_REQUEST
           response =  {
            "error": {
              "errorCode": 24,
              "statusCode": status.HTTP_400_BAD_REQUEST,
              "errorMessage": str(e)
            },
            "response": None
           }
           return Response(response, status=status_code)   

class ProfileDetailView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
       try:
          userId = request.user.id
          user_detail = Users.objects.filter(pk=userId).first()  
          response = {
            "error": None,
            "response": {
                   "data": {
                        'fullName' : user_detail.fullName,
                        'email' : user_detail.email,
                        'mobileNo' : user_detail.mobileNo,
                        'gender' : user_detail.gender,
                        'isActive' : user_detail.isActive,
                        'profileImage' : user_detail.image
                   },
              "message": {
                'success' : True,
                "successCode": 25,
                "statusCode": status.HTTP_200_OK,
                "successMessage": "User profile detail fetched successfully"
              }
            }
          }
          status_code = status.HTTP_200_OK
          return Response(response, status=status_code)    
       except Exception as e:
           status_code = status.HTTP_400_BAD_REQUEST
           response =  {
            "error": {
              "errorCode": 26,
              "statusCode": status.HTTP_400_BAD_REQUEST,
              "errorMessage": str(e)
            },
            "response": None
           }
           return Response(response, status=status_code)

class ProfileUpdateView(generics.UpdateAPIView):
    
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
           userId = request.user.id  
           request_data = JSONParser().parse(request)
           mobileNo = request_data['mobileNo']
           email = request_data['email']
           json_request = json.dumps(request_data)
           dictionary = json.loads(json_request) 
           check_user_if_exists = Users.objects.filter(pk=userId).first()
           if check_user_if_exists is None:
                  response = {
                   "error": {
                     "errorCode": 27,
                     "statusCode": status.HTTP_400_BAD_REQUEST,
                     "errorMessage": "Invalid user!"
                   },
                   "response": None
                  }
                  status_code = status.HTTP_200_OK
                  return Response(response, status=status_code)

           check_mobile_no_if_exists = Users.objects.filter(mobileNo=mobileNo).first()
           if check_mobile_no_if_exists is not None:
                response = {
                 "error": {
                   "errorCode": 1,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "mobileNo already exists!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)

           check_email_if_exists = Users.objects.filter(email=email).first()
           if check_email_if_exists is not None:
                response = {
                 "error": {
                   "errorCode": 2,
                   "statusCode": status.HTTP_400_BAD_REQUEST,
                   "errorMessage": "email already exists!"
                 },
                 "response": None
                }
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(response, status=status_code)
           
           usr = Users.objects.filter(pk=userId)
           if "fullName" in dictionary:
              usr.update(fullName=request_data['fullName'])
           if "email" in dictionary:
              usr.update(email=request_data['email'])
           if "mobileNo" in dictionary:
              usr.update(mobileNo=request_data['mobileNo'])
           if "gender" in dictionary:
              usr.update(gender=request_data['gender'])
           if "image" in dictionary:
              usr.update(image=request_data['image'])              

           user_detail = UserSerializer(usr,many=True)
           response = {
             "error": None,
             "response": {
                    "data": {
                         'updatedUserDetail' : user_detail.data
                    },
               "message": {
                 'success' : True,
                 "successCode": 28,
                 "statusCode": status.HTTP_200_OK,
                 "successMessage": "User profile updated successfully"
               }
             }
           }
           status_code = status.HTTP_200_OK
           return Response(response, status=status_code)

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response =  {
             "error": {
               "errorCode": 29,
               "statusCode": status.HTTP_400_BAD_REQUEST,
               "errorMessage": str(e)
             },
             "response": None
            }
        return Response(response, status=status_code)   