from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BooksModelViewSet

router = DefaultRouter()
router.register(r'books', BooksModelViewSet, basename='api')


app_name = 'books'
urlpatterns = [
    path('', include(router.urls)),
]
