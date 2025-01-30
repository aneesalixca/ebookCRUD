from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Main page with book list and form
    path('create/', views.book_list, name='book_create'),  # Create new book
    path('update/<int:id>/', views.book_list, name='book_update'),  # Update existing book
    path('delete/<int:id>/', views.book_delete, name='book_delete'),  # Delete book
]
