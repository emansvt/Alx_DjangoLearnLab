from django.urls import path
from . import views

urlpatterns = [
    # Task 3 RBAC routes
    path("admin-only/", views.admin_view, name="admin_view"),
    path("librarian-only/", views.librarian_view, name="librarian_view"),
    path("member-only/", views.member_view, name="member_view"),

    # Task 4 CRUD routes (permission-protected)
    path("books/", views.list_books, name="list_books"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
