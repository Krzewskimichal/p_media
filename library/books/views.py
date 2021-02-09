from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import BooksSerializer
from .models import Book


class BooksModelViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
