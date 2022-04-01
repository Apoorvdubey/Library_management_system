from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . serializers import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import boto3
import os
import uuid
from ebookReader import settings
from django.core.paginator import Paginator




loginDecorator = login_required(login_url='/users/login/')
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
        user = authenticate(request, email=email, password=password)

        if user:
            if user.userType=="admin":
                login(request, user)
                return redirect("/")
            else:
                messages.warning(request, 'Not authorised to perform this task')
                return redirect("login")
        else:
            messages.warning(request, 'User does not exists')
            return redirect('login')

    else:
        return render(request, "main/login.html", {})


def logut_admin(request):
    logout(request)
    return redirect("login")


@loginDecorator
def add_user(request):
    if request.method=="POST":
        email = request.POST.get('email')
        mobileNo = request.POST.get('mobileNo')
        gender = request.POST.get('inlineRadioOptions')
        fullName = request.POST.get('fullName')
        image = s3_helper(request.FILES.get('image'))
        password = make_password(request.POST.get('password'))

        check_email = Users.objects.filter(email=email).first()
        check_mobile_no = Users.objects.filter(mobileNo=mobileNo).first()
        if check_email:
            messages.warning(request, "User with this email is already registered")
            return redirect("/users/addUsers/")
        elif check_mobile_no:
            messages.warning(request, "User with this mobile number is already registered")
            return redirect("/users/addUsers/")
        else:
            Users.objects.create(email=email, mobileNo=mobileNo, gender=gender, image=image,  fullName=fullName, password=password)
            return redirect("/users/listUsers/id/")
    else:
        return render(request, "userManagement/add.html", {})


@loginDecorator
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


@loginDecorator
def delete_user(request, pk):

    instance = Users.objects.filter(pk=pk)
    instance.delete()
    return redirect("/users/listUsers/id/")


@loginDecorator
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

        if mobileNo != instance[0].mobileNo: 
            check_mobile_no = Users.objects.filter(mobileNo=mobileNo).first()
            if check_mobile_no:
                messages.warning(request, "User with this mobile number is already registered")
                return redirect("/users/editUser/" + pk + "/")
            else:
                instance.update(fullName=fullName, mobileNo=mobileNo, image=image, gender=gender)
                return redirect("/users/listUsers/id/")
        else:
            instance.update(fullName=fullName, mobileNo=mobileNo, image=image, gender=gender)
            return redirect("/users/listUsers/id/")
    else:
        instance = Users.objects.get(pk=pk)
        return render(request, "userManagement/edit.html", {"context":instance})


@loginDecorator
def block_unblock_user(request, pk):
    instance = Users.objects.filter(pk=pk)
    if instance[0].isActive==True:
        instance.update(isActive=False)
        return redirect("/users/listUsers/id/")
    else:
        instance.update(isActive=True)
        return redirect("/users/listUsers/id/")
    

@loginDecorator
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
        return render(request, "main/profile.html", {"context":instance})


@loginDecorator
def search_user(request):
    user_name = request.GET.get('search')
    instance = Users.objects.filter(fullName__icontains=user_name)
    p = Paginator(instance,4)
    page =  request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, "userManagement/index.html" ,{"venues": venues, "nums": 5, "search": user_name})