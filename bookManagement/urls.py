from django.urls import path, include
from . import views
from ebookReader import settings
from django.conf.urls.static import static


urlpatterns = [
    path("listBooks/<str:order>/", views.book_list, name="listBooks"),
    path("addBooks/", views.add_book, name="addBooks"),
    path("deleteBooks/<str:pk>/",  views.delete_book, name="deleteBooks"),
    path("searchBook/", views.search_book, name="searchBook"),
    path("bookAvailableUnavailable/<str:pk>/", views.book_available_unavailable, name="bookAvailableUnavailable"),
    path("editBook/<str:pk>/", views.edit_book, name="editBook"), 
    path('viewBookDetails/<str:pk>/', views.viewBookDetails, name="viewBookDetails"),
    path('removeBookImages/<str:pk>/', views.removeBookImages, name="removeBookImages")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)