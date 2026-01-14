from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('authors/', views.author_list, name='author-list'),
    path('libraries/', views.library_list, name='library-list'),
    path('librarians/', views.librarian_list, name='librarian-list'),
]

