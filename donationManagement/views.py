from django.shortcuts import render
from authAPIs.models import UserDonations
from django.core.paginator import Paginator
from django.utils.timezone import now
from datetime import datetime

# Create your views here.

def listDonations(request, order):

    instance = UserDonations.objects.all()
    if order=="createdAt":
        instance = UserDonations.objects.all().order_by(order).reverse()
    else:
        instance = UserDonations.objects.all().order_by(order)

    totalTransactions = instance.count()

    totalBalanceList = []
    for i in instance:
        if i.paymentStatus == 2:
            totalBalanceList.append(int(i.paymentAmount))
    totalBalance = sum(totalBalanceList)
    
    donerIdsList = []
    for i in instance:
        donerIdsList.append(i.userId)
    uniqueDonerIdsList = list(set(donerIdsList))
    totalDoners = len(uniqueDonerIdsList)
    
    newInstance = instance.filter(createdAt__date=datetime.now().date())
    newDonerIdsList = []
    for i in newInstance:
        newDonerIdsList.append(i.userId)
    uniqueNewDonerIdsList = list(set(newDonerIdsList))
    totalNewDoners = len(uniqueNewDonerIdsList)
    
    
    p = Paginator(instance,2)
    page =  request.GET.get('page')
    donations = p.get_page(page)
    return render(request, "donation/index.html", {"donations":donations, "totalTansactions": totalTransactions,
                                                    "totalBalance" : totalBalance, "totalDoners": totalDoners, 
                                                    "totalNewDoners": totalNewDoners})