from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django import forms
from django.db import models

# ------------------------------
# Simple Book model (Task 4 needs it here)
# If you already have Book elsewhere, remove this and import from there.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    published_year = models.PositiveIntegerField()

    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )

    def __str__(self):
        return self.title

# ------------------------------
# Forms for Book CRUD
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_year"]

# ------------------------------
# Helpers for role checks
def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"

# ------------------------------
# Task 3: Role-based views (function names exactly as requested)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")

# ------------------------------
# Task 4: Permission-protected CRUD
@login_required
@permission_required("django_models.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added.")
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})

@login_required
@permission_required("django_models.can_change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated.")
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form, "book": book})

@login_required
@permission_required("django_models.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted.")
        return redirect("list_books")
    return render(request, "books/delete_book.html", {"book": book})

@login_required
def list_books(request):
    qs = Book.objects.all().order_by("title")
    return render(request, "books/list_books.html", {"books": qs})
