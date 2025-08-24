<<<<<<< HEAD
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from django.http import HttpResponse
from .models import Author, Book, Librarian, Library

from django.contrib.auth.models import User

# Create your views here.

def booklist(request):
    books = Book.objects.all()
    context = {'books':books}

    return render(request, 'relationship_app/list_books.html',context=context)

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/librarylist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context


from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile

def has_role(user, role):
    return UserProfile.objects.filter(user=user.id, role=role).exists()
def is_admin(user):
    return has_role(user, "Admin")
def is_librarian(user):
    return has_role(user, "Librarian")
def is_member(user):
    return has_role(user, "Member")

# Views for Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# View for Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# View for Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class register(CreateView): 
    form_class = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'
    # user = self.get_object
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # user = self.get_object()
        context["user"] = self.request.user
        return context
    
from django.contrib.auth.views import LoginView, LogoutView

class login(LoginView):
    template_name = 'relationship_app/login.html'

class logout(LogoutView):
    template_name = 'relationship_app/logout.html'

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View for adding a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')  # Redirect to the book list view or another page

    return render(request, 'relationship_app/add_book.html')

# View for editing a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_list')

    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'relationship_app/delete_book.html', {'book': book})
=======
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm # adding/editing book

# Function-Based View (FBV)- Lists all books.
def list_books(request):
    books = Book.objects.all() # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) - Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member') # Create a UserProfile with default 'Member'
            return redirect('login') # Redirect to login after successful registration
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})

# Book Management Views
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'relationship_app.can_delete_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book.html', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Role Check Functions
def is_admin(user):
    return user.is_authenticated and (user.is_superuser or (hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'))

def is_librarian(user):
    return user.is_authenticated and (hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian')

def is_member(user):
    return user.is_authenticated and (hasattr(user, 'userprofile') and user.userprofile.role == 'Member')

# Admin View - Only accessible to Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

# Librarian View - Only accessible to Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')

# Member View - Only accessible to Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member.html')
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
