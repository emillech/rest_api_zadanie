from rest_framework import serializers
from .models import Author, Book, Publisher


class BookSerializer(serializers.Serializer):
    author = serializers.SlugRelatedField(many=True, slug_field='nickname', queryset=Author.objects.all())
    publisher = serializers.SlugRelatedField(slug_field='name', queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'author', 'publisher', 'pages_num', 'cover_image')
