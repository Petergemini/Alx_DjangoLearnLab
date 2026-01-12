import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Library

author_name = "Chinua Achebe"
library_name = "Nairobi Public Library"

author = Author.objects.get(name=author_name)
print(f"Books by {author_name}:")
for book in author.books.all():
    print(f"- {book.title}")

library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(f"- {book.title}")

librarian = library.librarian
print(f"\nLibrarian for {library_name}:")
print(f"- {librarian.name}")
