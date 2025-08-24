from django.urls import path
<<<<<<< HEAD
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]
=======
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
from .views import BookListCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-delete'),
    # List all books and create a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # Retrieve a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book (if you want a separate view for this, though it's combined in ListCreate)
    path('books/create/', BookListCreateView.as_view(), name='book-create'),

    # Update a book by its ID
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book by its ID
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]


 

 

 

 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
