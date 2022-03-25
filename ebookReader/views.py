from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Users
from bookManagement.models import Book


# Create your views here.
@login_required(login_url='/users/login/')
def index(request):
    totalUsers = Users.objects.filter(isDeleted=False).count()
    totalBooks = Book.objects.all().count()
    print(totalUsers, totalBooks)
    return render(request, "main/dashboard.html", context={"totalUsers": totalUsers, "totalBooks": totalBooks})
