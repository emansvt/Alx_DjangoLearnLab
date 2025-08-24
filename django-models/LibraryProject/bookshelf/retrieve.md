<<<<<<< HEAD
# Retrieve the Book instance

## Command:
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book)

1984 by George Orwell (1949)
=======
### Retrieve Operation

Command:
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book)
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
