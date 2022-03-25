from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Users
from bookManagement.models import Book
from users.views import loginDecorator

# Create your views here.
@loginDecorator
def index(request):
    totalUsers = Users.objects.filter(isDeleted=False).count()
    totalBooks = Book.objects.all().count()
    return render(request, "main/dashboard.html", context={"totalUsers": totalUsers, "totalBooks": totalBooks})
