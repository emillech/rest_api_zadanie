from rest_framework import serializers
from .models import Author, Book, Publisher, BookAuthor


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.SlugRelatedField(slug_field='name', queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'title', 'cover_image', 'publisher')


class BookDetailsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, slug_field='nickname', queryset=Author.objects.all())
    publisher = serializers.SlugRelatedField(slug_field='name', queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class BookRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookOfAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


