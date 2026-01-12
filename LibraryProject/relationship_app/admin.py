from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models so they appear in Django Admin
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

