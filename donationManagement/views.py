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
    totalBalance = sum([int(x.paymentAmount) for x in instance if x.paymentStatus == 2])
    totalDoners = len(list(set([x.userId for x in instance])))

    newInstance = instance.filter(createdAt__date=datetime.now().date())
    totalNewDoners = len(list(set([x.userId for x in newInstance])))
    
    totalLastMonthDoners = len(list(set([x.userId for x in UserDonations.objects.filter(createdAt__month=datetime.now().month-1)])))
    
    d = {}
    for i in range(0,12):
        d[i]=UserDonations.objects.filter(createdAt__month=i)
    monthsList = [0, sum([int(x.paymentAmount) for x in d[0]]), sum([int(x.paymentAmount) for x in d[1]]), 
                sum([int(x.paymentAmount) for x in d[2]]), sum([int(x.paymentAmount) for x in d[3]]), 
                sum([int(x.paymentAmount) for x in d[4]]), sum([int(x.paymentAmount) for x in d[5]]), 
                sum([int(x.paymentAmount) for x in d[6]]), sum([int(x.paymentAmount) for x in d[7]]),
                sum([int(x.paymentAmount) for x in d[8]]), sum([int(x.paymentAmount) for x in d[9]]),
                sum([int(x.paymentAmount) for x in d[10]]), sum([int(x.paymentAmount) for x in d[11]])]

    p = Paginator(instance, 3)
    page =  request.GET.get('page')
    donations = p.get_page(page)
    return render(request, "donation/index.html", {"donations":donations, "totalTansactions": totalTransactions,
                                                    "totalBalance" : totalBalance, "totalDoners": totalDoners, 
                                                    "totalNewDoners": totalNewDoners, "monthsList": monthsList})


def listLastMonthDonations(request, order):
    print(datetime.now().month)

    instance = UserDonations.objects.filter(createdAt__month=datetime.now().month-1)
    if order=="createdAt":
        instance = UserDonations.objects.filter(createdAt__month=datetime.now().month-1).order_by(order).reverse()
    else:
        instance = UserDonations.objects.filter(createdAt__month=datetime.now().month-1).order_by(order)

    totalTransactions = UserDonations.objects.all().count()
    totalBalance = sum([int(x.paymentAmount) for x in UserDonations.objects.all() if x.paymentStatus == 2])
    totalDoners = len(list(set([x.userId for x in UserDonations.objects.all()])))

    newInstance = UserDonations.objects.filter(createdAt__date=datetime.now().date())
    totalNewDoners = len(list(set([x.userId for x in newInstance])))
    totalLastMonthDoners = len(list(set([x.userId for x in instance])))
    
    newInstance = instance.filter(createdAt__date=datetime.now().date())
    
    d = {}
    for i in range(0,12):
        d[i]=UserDonations.objects.filter(createdAt__month=i)
    monthsList = [0, sum([int(x.paymentAmount) for x in d[0]]), sum([int(x.paymentAmount) for x in d[1]]), 
                sum([int(x.paymentAmount) for x in d[2]]), sum([int(x.paymentAmount) for x in d[3]]), 
                sum([int(x.paymentAmount) for x in d[4]]), sum([int(x.paymentAmount) for x in d[5]]), 
                sum([int(x.paymentAmount) for x in d[6]]), sum([int(x.paymentAmount) for x in d[7]]),
                sum([int(x.paymentAmount) for x in d[8]]), sum([int(x.paymentAmount) for x in d[9]]),
                sum([int(x.paymentAmount) for x in d[10]]), sum([int(x.paymentAmount) for x in d[11]])]

    p = Paginator(instance, 3)
    page =  request.GET.get('page')
    donations = p.get_page(page)
    return render(request, "donation/lastMonthIndex.html", {"donations":donations, "totalTansactions": totalTransactions,
                                                    "totalBalance" : totalBalance, "totalDoners": totalDoners, 
                                                    "totalNewDoners": totalNewDoners, "monthsList": monthsList,
                                                    'totalLastMonthDoners': totalLastMonthDoners})