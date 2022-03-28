from django.shortcuts import render
from authAPIs.models import UserDonations
from django.core.paginator import Paginator

# Create your views here.

def listDonations(request, order):

    instance = UserDonations.objects.all()
    if order=="createdAt":
        instance = UserDonations.objects.all().order_by(order).reverse()
    else:
        instance = UserDonations.objects.all().order_by(order)

    p = Paginator(instance,2)
    page =  request.GET.get('page')
    donations = p.get_page(page)
    return render(request, "donation/index.html", {"donations":donations})