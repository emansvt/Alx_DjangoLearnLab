<<<<<<< HEAD
# Delete the Book instance

## Command:
```python
retrieved_book.delete()
print(Book.objects.all())

<QuerySet []>

"book.delete", "from bookshelf.models import Book"
=======
### Delete Operation

Command:
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.delete()
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
