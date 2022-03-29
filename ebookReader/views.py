from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authAPIs.models import UserDonations
from users.models import Users
from bookManagement.models import Book
from users.views import loginDecorator
from datetime import datetime

# Create your views here.
@loginDecorator
def index(request):
    totalUsers = Users.objects.filter(isDeleted=False).count()
    totalBooks = Book.objects.all().count()
    totalDoners = len(list(set([x.userId for x in UserDonations.objects.all()])))
    totalLastMonthDoners = len(list(set([x.userId for x in UserDonations.objects.filter(createdAt__month=datetime.now().month-1)])))
    return render(request, "main/dashboard.html", context={"totalUsers": totalUsers, "totalLastMonthDoners": totalLastMonthDoners,
                                                            "totalBooks": totalBooks, "totalDoners": totalDoners})
