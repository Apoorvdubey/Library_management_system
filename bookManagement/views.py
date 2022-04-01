from gettext import install
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from users.views import s3_helper, loginDecorator
# Create your views here.


@loginDecorator
def book_list(request, order):

    instance = Book.objects.all().order_by(order)

    p = Paginator(instance,3)
    
    page =  request.GET.get('page')
    
    books = p.get_page(page)
    
    nums = "a" * books.paginator.num_pages
    return render(request, "bookManagement/index.html", {"books": books, "nums": nums})


@loginDecorator
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
        bookImages = request.FILES.getlist('bookImages')
    
        instance = Book.objects.create(name=name, bookCover=s3_helper(bookCover), description=description, isAvailable=isAvailable, author=author, authorDescription=authonDescription, price=price, file=s3_helper(file))
        for i in bookImages:
            BookImages.objects.create(bookImage=s3_helper(i), bookId=instance)
        return redirect("/bookManagement/listBooks/id/")

    else:
        return render(request, "bookManagement/add.html", {})


@loginDecorator
def delete_book(request, pk):
    instance = Book.objects.filter(pk=pk)
    instance.delete()
    return redirect("/bookManagement/listBooks/id/")


@loginDecorator
def search_book(request):
    book_name = request.GET.get('search')
    instance = Book.objects.filter(name__icontains=book_name)
    p = Paginator(instance,4)
    page =  request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, "bookManagement/index.html", {"books": venues, "nums":5, "search": book_name})


@loginDecorator
def book_available_unavailable(request, pk):
    instance = Book.objects.filter(pk=pk)
    if instance[0].isAvailable==True:
        instance.update(isAvailable=False)
        return redirect("/bookManagement/listBooks/id/")
    else:
        instance.update(isAvailable=True)
        return redirect("/bookManagement/listBooks/id/")


@loginDecorator
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


@loginDecorator
def viewBookDetails(request, pk):

    try:
        instance = Book.objects.get(pk=pk)
        imageInstance = BookImages.objects.filter(bookId=instance)
        return render(request, "bookManagement/view.html", context = {"Book": instance, "imageInstance": imageInstance})
    except:
        return redirect("/bookManagement/listBooks/id/")


@loginDecorator
def removeBookImages(request, pk):
    try:
        imageInstance = BookImages.objects.get(pk=pk)
        imageInstance.delete()
        return redirect("/bookManagement/editBook/" + str(imageInstance.bookId.pk) + "/")
    except:
        imageInstance = BookImages.objects.get(pk=pk)
        return redirect("/bookManagement/editBook/" + str(imageInstance.bookId.pk) + "/")
        