from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    birthdate = models.DateField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    pages_num = models.IntegerField()
    cover_image = models.ImageField()

    def __str__(self):
        return self.title
