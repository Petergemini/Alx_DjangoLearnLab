import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "Chinua Achebe"

author = Author.objects.filter(name=author_name).first()

print(f"Books by {author_name}:")
for book in Book.objects.filter(author=author):
    print(f"- {book.title}")

library_name = "Nairobi Public Library"
library = Library.objects.filter(name=library_name).first()

print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(f"- {book.title}")

print(f"\nLibrarian for {library_name}:")
for librarian in Librarian.objects.filter(library=library):
    print(f"- {librarian.name}")

