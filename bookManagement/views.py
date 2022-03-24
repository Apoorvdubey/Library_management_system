from gettext import install
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from users.views import s3_helper
# Create your views here.


class ListBookView(APIView):
    """"
    API for listing all the uploaded books with details
    """
    serializers_class = BookListSerializer

    def get(self, request):
        instance =  Book.objects.all()
        serializers = self.serializers_class(instance=instance, many=True)
        return Response({"response_message":"Books fetched successfully", "count": instance.count(), "data": serializers.data}, status=status.HTTP_200_OK)



@login_required(login_url='/users/login/')
def book_list(request, order):

    instance = Book.objects.all().order_by(order)

    p = Paginator(instance,2)
    
    page =  request.GET.get('page')
    
    books = p.get_page(page)
    
    nums = "a" * books.paginator.num_pages
    return render(request, "bookManagement/index.html", {"books": books, "nums": nums})


@login_required(login_url='/users/login/')
def add_book(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        bookCover = request.FILES.get('bookCover')
        description = request.POST.get('description')
        author = request.POST.get('author')
        authonDescription = request.POST.get('authorDescription')
        price = request.POST.get('price')
        file = request.FILES.get('file')
        isAvailable = request.POST.get('isAvailable')
    
        Book.objects.create(name=name, bookCover=s3_helper(bookCover), description=description, isAvailable=isAvailable, author=author, authorDescription=authonDescription, price=price, file=s3_helper(file))
        return redirect("/bookManagement/listBooks/id/")

    else:
        return render(request, "bookManagement/add.html", {})


@login_required(login_url='/users/login/')
def delete_book(request, pk):
    instance = Book.objects.filter(pk=pk)
    instance.delete()
    return redirect("/bookManagement/listBooks/id/")


@login_required(login_url='/users/login/')
def search_book(request):
    book_name = request.GET.get('search')
    instance = Book.objects.filter(name__icontains=book_name)
    return render(request, "bookManagement/index.html", {"books": instance, "nums":5})


@login_required(login_url='/users/login/')
def book_available_unavailable(request, pk):
    instance = Book.objects.filter(pk=pk)
    if instance[0].isAvailable==True:
        instance.update(isAvailable=False)
        return redirect("/bookManagement/listBooks/id/")
    else:
        instance.update(isAvailable=True)
        return redirect("/bookManagement/listBooks/id/")


def edit_book(request, pk):
    if request.method == "POST":
        name = request.POST.get('name')
        bookCover = request.FILES.get('bookCover')
        description = request.POST.get('description')
        author = request.POST.get('author')
        authorDescription = request.POST.get('authorDescription')
        price = request.POST.get('price')
        file = request.FILES.get('file')
        isAvailable = request.POST.get('isAvailable')
        
        instance = Book.objects.filter(pk=pk)

        currentCover = instance[0].bookCover
        if bookCover is None:
            bookCover = currentCover
        else:
            bookCover = s3_helper(bookCover)

        currentFile = instance[0].file
        if file is None:
            file = currentFile
        else:
            file = s3_helper(file)

        instance.update(name=name, bookCover=bookCover, description=description, author=author, authorDescription=authorDescription,
                price=price, file=file, isAvailable=isAvailable)
        return redirect("/bookManagement/listBooks/id/")
    else:
        instance = Book.objects.get(pk=pk)
        return render(request, "bookManagement/edit.html", {"context":instance})
