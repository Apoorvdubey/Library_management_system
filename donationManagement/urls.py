from django.urls import path
from . import views


urlpatterns = [

    path("listDonations/<str:order>/", views.listDonations, name="listDonations"),
    
]