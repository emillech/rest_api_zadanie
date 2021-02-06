from .models import Book
from .serializers import BookSerializer, BookDetailsSerializer
from rest_framework import generics


class BooksListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer

