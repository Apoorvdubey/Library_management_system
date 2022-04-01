from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.login_admin, name="login"),
    path("logout/", views.logut_admin, name="logout"),
    path("listUsers/<str:order>/", views.user_list, name="listUsers"),
    path("addUsers/", views.add_user, name="addUsers"),
    path("deleteUser/<str:pk>/", views.delete_user, name="deleteUser"),
    path("editAdminProfile/", views.profile_view, name="editAdminProfile"),
    path("searchUser/", views.search_user, name="searchUser"),
    path('blockUnblockUser/<str:pk>/', views.block_unblock_user, name="blockUnblockUser"),
    path("editUser/<str:pk>/", views.edit_user, name="editUser"),
]