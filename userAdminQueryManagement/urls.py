from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("listQueries/<str:order>/", views.listQueries, name="listQueries"),
    path("viewQuery/<str:pk>/", views.viewQuery, name="viewQuery"),

]
