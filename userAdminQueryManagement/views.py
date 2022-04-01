from django.shortcuts import redirect, render
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


@loginDecorator
def viewQuery(request, pk):
    instance = UserAdminQueriesContents.objects.filter(userAdminQueryId=pk)
    return render(request, "userAdminQueries/view.html",{"context":instance,})


@loginDecorator
def replyUserQuery(request, pk):
    if request.method=="POST":
        reply = request.POST.get('reply')
        instance = UserAdminQueries.objects.get(userAdminQueryId=pk)
        UserAdminQueriesContents.objects.create(userAdminQueryId=instance, message=reply, isSentByAdmin=True)
        if instance.queryStatus == 'pending':
            instance.queryStatus = "open"
            instance.save()
        contentInstance = UserAdminQueriesContents.objects.filter(userAdminQueryId=pk)
        return render(request, "userAdminQueries/view.html", {"context":contentInstance})
    else: 
        instance = UserAdminQueriesContents.objects.filter(userAdminQueryId=pk)
        return render(request, "userAdminQueries/view.html", {"context":instance,})



from ebookReader import settings
@loginDecorator
def updateUserQueryStatus(request, pk, queryStatus):
    
    instance = UserAdminQueries.objects.get(pk=pk)
    instance.queryStatus = queryStatus
    instance.save()
    if request.__dict__['META']['HTTP_REFERER'] == "http://127.0.0.1:8000/userAdminQueryManagement/listQueries/createdAt/":
        return redirect("/userAdminQueryManagement/listQueries/createdAt/")
    else:
        return redirect("/userAdminQueryManagement/viewQuery/" + pk + "/")