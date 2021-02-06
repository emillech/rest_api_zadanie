from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ManyToManyField("Author", through="BookAuthor")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    pages_num = models.IntegerField()
    cover_image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)