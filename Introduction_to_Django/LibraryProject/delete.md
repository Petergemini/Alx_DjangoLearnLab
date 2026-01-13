# Delete Operation

from books.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output: (1, {'books.Book': 1})
Book.objects.all()
# Output: <QuerySet []>
