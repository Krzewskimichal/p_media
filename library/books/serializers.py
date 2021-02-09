from rest_framework.serializers import ModelSerializer

from .models import Book, Author, Publisher


class BooksSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.pages_num = validated_data.get('pages_num', instance.pages_num)
    #     instance.publisher = validated_data.get('publisher', instance.publisher)
    #     instance.save()
    #     return instance


class AuthorsSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublishersSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'
