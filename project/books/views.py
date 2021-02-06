from .models import Book, Publisher
from .serializers import BookSerializer, BookDetailsSerializer, PublisherSerializer
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
