from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import Book, Author, Publisher


class BooksModelViewSet(ModelViewSet):
    serializer_class = BookSerializer
    detail_serializer_class = BooksDetailSerializer
    list_serializer_class = BooksListSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(ModelViewSet, self).get_serializer_class()

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Author.objects.all()

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorsSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        publisher = self.get_object(pk)
        serializer = AuthorsSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherModelViewSet(ModelViewSet):
    serializer_class = PublishersSerializer
    queryset = Publisher.objects.all()

    def put(self, request, pk, format=None):
        publisher = self.get_object(pk)
        serializer = PublishersSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        publisher = self.get_object(pk)
        serializer = PublishersSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        publisher = self.get_object(pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
