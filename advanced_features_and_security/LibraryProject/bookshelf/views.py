<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render, redirect
from .forms import ExampleForm 

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  
    return render(request, 'bookshelf/book_list.html', {'books': books})

def index(request):
    return HttpResponse("Welcome to my book store.")

# Create your views here.

def some_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success_url')  
=======
from django.shortcuts import render, redirect
from .models import Book
from .forms import ExampleForm  # Import the form

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after successful form submission
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
