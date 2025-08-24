from rest_framework import serializers
<<<<<<< HEAD
from .models import Author, Book
import datetime
=======
from .models import Book 
from .models import Book, Author
from datetime import datetime 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
<<<<<<< HEAD
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
=======
        fields = '__all__'
 # For checking the current year

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Add custom validation to check the publication year
    def validate_publication_year(self, value):
        if value > datetime.now().year:
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
<<<<<<< HEAD

=======
    # Nesting BookSerializer to serialize related books dynamically
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
<<<<<<< HEAD
        fields = ['id', 'name', 'books']

#The BookSerializer is the serialization of the Book model. It includes a custom validation to ensure that the publication year is not in the future.

#The AuthorSerializer includes a nested representation of related books using the BookSerializer. This allows authors to be serialized with their associated books.
=======
        fields = ['name', 'books']
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
