from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("users/", include("users.urls"), name="users"),
    path("", views.index, name="index"),
    path("bookManagement/", include("bookManagement.urls"), name="bookManagement"),
    path('v1/api/', include('authAPIs.urls')),
]
