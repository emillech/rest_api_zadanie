from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ManyToManyField("Author", through="BookAuthor")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    pages_num = models.IntegerField()
    cover_image = models.ImageField()


class Publisher(models.Model):
    name = models.CharField(max_length=64)


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    birth_date = models.DateField()


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)