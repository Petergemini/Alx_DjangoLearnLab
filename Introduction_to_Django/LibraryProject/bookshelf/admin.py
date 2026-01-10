from django.contrib import admin
from .models import Book

<<<<<<< HEAD

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
=======
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)
>>>>>>> 02f82937dad22993b12d55292de4307ff018b07e

