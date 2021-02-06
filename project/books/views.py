from .models import Book
from .serializers import BookSerializer, BookDetailsSerializer
from rest_framework import viewsets


class BooksListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        return BookDetailsSerializer



