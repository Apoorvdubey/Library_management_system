from django.shortcuts import render
from .models import UserAdminQueriesContents, UserAdminQueries
from django.core.paginator import Paginator
from users.views import loginDecorator

# Create your views here.


@loginDecorator
def listQueries(request, order):
    if order=="createdAt":
        instance = UserAdminQueries.objects.all().order_by(order).reverse()
    else:
        instance = UserAdminQueries.objects.all().order_by(order)

    p = Paginator(instance,2)
    page =  request.GET.get('page')
    queries = p.get_page(page)

    return render(request, "userAdminQueries/index.html", {"queries" : queries })


def viewQuery(request, pk):
    if request.method=="POST":
        pass
    else:
        return render(request, "userAdminQueries/view.html",{})