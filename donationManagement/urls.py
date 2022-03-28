from django.urls import path
from . import views


urlpatterns = [

    path("listDonations/createdAt/", views.listDonations, name="listDonations"),
    
]