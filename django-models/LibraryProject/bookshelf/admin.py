from django.contrib import admin
from .models import Book

<<<<<<< HEAD
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters to allow quick sorting and categorization
    list_filter = ('publication_year', 'author')

    # Search capability by title and author
    search_fields = ('title', 'author')

=======
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

# Bookwarm | warmth@gmail.com | warm4real
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
