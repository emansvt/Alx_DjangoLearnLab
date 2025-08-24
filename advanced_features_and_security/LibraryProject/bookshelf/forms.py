from django import forms
<<<<<<< HEAD
from .models import Book 

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search Query')

  
=======
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search Books')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
 
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
