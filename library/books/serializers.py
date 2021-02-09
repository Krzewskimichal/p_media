from rest_framework.serializers import ModelSerializer, Serializer, CharField

from .models import Book, Author, Publisher


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublishersSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookDetailsAuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname']


class BookDetailPublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']


class BooksDetailSerializer(ModelSerializer):
    publisher = BookDetailPublisherSerializer()
    author = BookDetailsAuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'pages_num', 'author', 'publisher']


class BooksListSerializer(ModelSerializer):
    publisher = BookDetailPublisherSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'cover_image', 'publisher')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
