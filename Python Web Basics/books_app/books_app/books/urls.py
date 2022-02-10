from django.urls import path

from books_app.books.views import index, update_book, create_book

urlpatterns = [
    path('', index, name='home page'),
    path('update/<int:pk>', update_book, name='update book'),
    path('create/', create_book, name='create book'),
]