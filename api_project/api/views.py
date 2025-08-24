<<<<<<< HEAD
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

class BookViewSet(viewsets.ModelViewSet):
    
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
=======
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
 
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

 

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
