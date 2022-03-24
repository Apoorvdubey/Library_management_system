from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.login_admin, name="login"),
    path("logout/", views.logut_admin, name="logout"),
    path("usersList/", views.UsersListView.as_view(), name="usersList"),
    # path("deleteUser/<str:pk>/", views.DeleteUsersView.as_view(), name="deleteUser"),
    # path("editUser/<str:pk>/", views.EditUsersView.as_view(), name="editUser"),
    path("searchUsers/", views.SearchUserView.as_view(), name="searchUsers"),
    path("createUser/", views.CreateUserView.as_view(), name="createUser"),
    # path("blockUnblockUser/<str:pk>/", views.BlockUnblockUsersView.as_view(), name="blockUnblockUser"),

    path("listUsers/<str:order>/", views.user_list, name="listUsers"),
    path("addUsers/", views.add_user, name="addUsers"),
    path("deleteUser/<str:pk>/", views.delete_user, name="deleteUser"),

    path("profile/", views.profile_view, name="profile"),

    path("searchUser/", views.search_user, name="searchUser"),

    path('blockUnblockUser/<str:pk>/', views.block_unblock_user, name="blockUnblockUser"),

    path("editUser/<str:pk>/", views.edit_user, name="editUser"),


]