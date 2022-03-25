from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.views import APIView
from . serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.contrib.auth.decorators import login_required
import boto3
import os
import uuid
from ebookReader import settings
from django.core.paginator import Paginator

from users import serializers


# Create your views here.


def s3_helper(file):
    s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY, 
                              aws_secret_access_key=settings.AWS_SECRET_KEY,
                              region_name=settings.REGION_NAME
                              )

    bucket = s3.Bucket(settings.S3_BUCKET)
    split_tup = os.path.splitext(file.name)
    file_extension = split_tup[1]
    new_file_name = "image"+str(uuid.uuid4())[:8]+file_extension
    bucket.put_object(Key=new_file_name, Body=file)
    file_url = 'https://ebook-dev.s3.amazonaws.com/'+new_file_name
    return file_url


def login_admin(request):
    if request.method=="POST":
        email = request.POST['email-username']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)

        if user:
            if user.userType=="admin":
                login(request, user)
                print("1 is working")
                return redirect("/")
            else:
                messages.warning(request, 'Not authorised to perform this task')
                print("2 is working")
                return redirect("login")
        else:
            messages.warning(request, 'User does not exists')
            print("3 is working")
            return redirect('login')

    else:
        return render(request, "main/login.html", {})


def logut_admin(request):
    logout(request)
    return redirect("login")


class CreateUserView(APIView):
    """
    API for creating new user via admin
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        params = request.data
        instance = Users.objects.all()
        try:
            instance.create(email=params['email'],
                            mobileNo=params['mobileNo'],
                            gender=params['gender'],
                            fullName=params["fullName"],
                            password=make_password(params['password']))
            return Response({"response_message":"User created successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"response_message":"Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='/users/login/')
def add_user(request):
    if request.method=="POST":
        email = request.POST.get('email')
        mobileNo = request.POST.get('mobileNo')
        gender = request.POST.get('inlineRadioOptions')
        fullName = request.POST.get('fullName')
        image = s3_helper(request.FILES.get('image'))
        password = make_password(request.POST.get('password'))

        Users.objects.create(email=email, mobileNo=mobileNo, gender=gender, image=image,  fullName=fullName, password=password)
        return redirect("/users/listUsers/id/")
    else:
        return render(request, "userManagement/add.html", {})


class UsersListView(APIView, LimitOffsetPagination):
    """
    API for listing all users
    """
    serializers_class = UserListSerializer
    permission_classes = [IsAuthenticated]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'main/home.html'

    def get(self, request):
        instance = Users.objects.filter(userType="user")
        results = self.paginate_queryset(instance, request, view=self)
        serializers = self.serializers_class(instance=results, many= True)
        return Response({"response_message":"Data fetched successfully", "count": instance.count(), "data":serializers.data}, status=status.HTTP_200_OK)



@login_required(login_url='/users/login/')
def user_list(request, order):

    if order=="id" or order=="createdAt":
        instance = Users.objects.filter(userType='user').order_by(order).reverse()
    else:
        instance = Users.objects.filter(userType='user').order_by(order)

    p = Paginator(instance,4)
    
    page =  request.GET.get('page')
    
    venues = p.get_page(page)
    
    nums = "a" * venues.paginator.num_pages

    return render(request, "userManagement/index.html", {"venues": venues, "nums": nums})


class DeleteUsersView(APIView):
    """
    API for deleting a user
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        instance = Users.objects.filter(pk=pk)
        if instance:
            instance.delete()
            return Response({"response_message":"User deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"response_message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@login_required(login_url='/users/login/')
def delete_user(request, pk):

    instance = Users.objects.filter(pk=pk)
    instance.delete()
    return redirect("/users/listUsers/id/")


class EditUsersView(APIView):
    """
    API for editing a user
    """
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        params = request.data
        instance = Users.objects.filter(pk=pk)
        if instance:
            instance.update(fullName=params['fullName'], gender=params["gender"])
            return Response({"response_message":"User updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"response_message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@login_required(login_url='/users/login/')
def edit_user(request, pk):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        mobileNo = request.POST.get('mobileNo')
        gender = request.POST.get('inlineRadioOptions')
        image = request.FILES.get('image')
        
        instance = Users.objects.filter(pk=pk)
        currentImage = instance[0].image
        if image is None:
            image = currentImage
        else:
            image = s3_helper(image)
        instance.update(fullName=fullName, mobileNo=mobileNo, image=image, gender=gender)
        return redirect("/users/listUsers/id/")
    else:
        instance = Users.objects.get(pk=pk)
        return render(request, "userManagement/edit.html", {"context":instance})
            

class BlockUnblockUsersView(APIView):
    """
    API for blocking and unblocking a user
    """
    permission_classes = [IsAuthenticated]

    def put(sef, request, pk):
        instance = Users.objects.filter(pk=pk)
        if instance:
            if instance[0].isActive==True:
                instance.update(isActive=False)
                return Response({"response_message":"User blocked successfully"}, status=status.HTTP_200_OK)
            else:
                instance.update(isActive=True)
                return Response({"response_message":"User unblocked successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"response_message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@login_required(login_url='/users/login/')
def block_unblock_user(request, pk):
    instance = Users.objects.filter(pk=pk)
    if instance[0].isActive==True:
        instance.update(isActive=False)
        return redirect("/users/listUsers/id/")
    else:
        instance.update(isActive=True)
        return redirect("/users/listUsers/id/")
    

@login_required(login_url='/users/login/')
def profile_view(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        mobileNo = request.POST.get('mobileNo')
        # gender = request.POST.get('inlineRadioOptions')
        image = request.FILES.get('image')
        
        instance = Users.objects.filter(pk=request.user.pk)
        currentImage = instance[0].image
        if image is None:
            image = currentImage
        else:
            image = s3_helper(image)
        instance.update(fullName=fullName, mobileNo=mobileNo, image=image,)
        return redirect("/")
    else:
        instance = Users.objects.get(pk=request.user.pk)
        return render(request, "main/profile.html", {"context":instance} )


class SearchUserView(APIView):
    """
    API for searching users
    """
    serializers_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        params = request.data
        instance = Users.objects.filter(fullName__icontains=params['search'])
        serializers = self.serializers_class(instance=instance, many=True)
        return Response({"response_message": "Users fetched successfully", "data":serializers.data}, status=status.HTTP_200_OK)
        


@login_required(login_url='/users/login/')
def search_user(request):
    user_name = request.GET.get('search')
    instance = Users.objects.filter(fullName__icontains=user_name)
    print("instance ", instance)
    return render(request, "userManagement/index.html" ,{"venues": instance, "nums": 5})

