from rest_framework.response import Response
from .models import Book, Publisher, Author
from .serializers import BookSerializer, BookDetailsSerializer, PublisherSerializer, AuthorSerializer, \
    BookRetrieveSerializer, BookOfAuthorSerializer
from rest_framework import viewsets


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        elif self.action == 'retrieve':
            return BookRetrieveSerializer
        return BookDetailsSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        books = Book.objects.filter(author=instance)
        books_serializer = []
        for book in books:
            books_serializer.append(BookOfAuthorSerializer(book).data)
        result = [serializer.data, books_serializer]
        return Response(result)




