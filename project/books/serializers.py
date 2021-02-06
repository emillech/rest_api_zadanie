from rest_framework import serializers
from .models import Author, Book, Publisher


class BookSerializer(serializers.Serializer):
    author = serializers.SlugRelatedField(many=True)
    publisher = serializers.SlugRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'author', 'publisher', 'pages_num', 'cover_image')
