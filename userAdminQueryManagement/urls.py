from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("listQueries/<str:order>/", views.listQueries, name="listQueries"),
    path("viewQuery/<str:pk>/", views.viewQuery, name="viewQuery"),
    path("replyUserQuery/<str:pk>/", views.replyUserQuery, name="replyUserQuery"),
    path("updateUserQueryStatus/<str:pk>/<str:queryStatus>/", views.updateUserQueryStatus, name="updateUserQueryStatus"),
]
