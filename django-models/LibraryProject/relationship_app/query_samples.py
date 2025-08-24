<<<<<<< HEAD
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None


# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # Returns all books related to the library
    except Library.DoesNotExist:
        return None


# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Librarian.objects.get(library=library_name)
        return Librarian.library  # Returns the librarian related to the library
    except Library.DoesNotExist:
        return None
=======
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return [book.title for book in books]

# Retrieve the librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian.name

# Example Usage
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':", books_by_author("J.K. Rowling"))
    print("Books in Library 'City Library':", books_in_library("City Library"))
    print("Librarian of 'City Library':", get_librarian("City Library"))

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
