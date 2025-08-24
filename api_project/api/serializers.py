from rest_framework import serializers
from .models import Book

<<<<<<< HEAD

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
=======
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
