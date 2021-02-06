from .models import Book, Publisher, Author
from .serializers import BookSerializer, BookDetailsSerializer, PublisherSerializer, AuthorSerializer
from rest_framework import viewsets


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        return BookDetailsSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
