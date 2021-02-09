from rest_framework.serializers import ModelSerializer

from .models import Book, Author, Publisher


class BooksSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorsSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublishersSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'
