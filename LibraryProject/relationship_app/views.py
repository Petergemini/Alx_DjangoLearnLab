from django.http import HttpResponse
from .models import Book, Author, Library, Librarian

def book_list(request):
    books = Book.objects.all()
    titles = ', '.join([book.title for book in books])
    return HttpResponse(f"Books: {titles}")

def author_list(request):
    authors = Author.objects.all()
    names = ', '.join([author.name for author in authors])
    return HttpResponse(f"Authors: {names}")

def library_list(request):
    libraries = Library.objects.all()
    names = ', '.join([library.name for library in libraries])
    return HttpResponse(f"Libraries: {names}")

def librarian_list(request):
    librarians = Librarian.objects.all()
    info = ', '.join([f"{lib.name} at {lib.library.name}" for lib in librarians])
    return HttpResponse(f"Librarians: {info}")
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian

def home_view(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    libraries = Library.objects.all()
    librarians = Librarian.objects.all()
    
    context = {
        'authors': authors,
        'books': books,
        'libraries': libraries,
        'librarians': librarians,
    }
    return render(request, 'relationship_app/home.html', context)

def book_list(request):
    books = Book.objects.all()
    titles = ', '.join([book.title for book in books])
    return HttpResponse(f"Books: {titles}")

def author_list(request):
    authors = Author.objects.all()
    names = ', '.join([author.name for author in authors])
    return HttpResponse(f"Authors: {names}")

def library_list(request):
    libraries = Library.objects.all()
    names = ', '.join([library.name for library in libraries])
    return HttpResponse(f"Libraries: {names}")

def librarian_list(request):
    librarians = Librarian.objects.all()
    info = ', '.join([f"{lib.name} at {lib.library.name}" for lib in librarians])
    return HttpResponse(f"Librarians: {info}")

