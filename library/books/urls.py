from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BooksModelViewSet, AuthorModelViewSet, PublisherModelViewSet

router = DefaultRouter()
router.register(r'books', BooksModelViewSet, basename='books')
router.register(r'authors', AuthorModelViewSet, basename='authors')
router.register(r'publishers', PublisherModelViewSet, basename='publishers')

app_name = 'books'
urlpatterns = [
    path('', include(router.urls)),
]
