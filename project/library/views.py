from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from library.models import Book
from library.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'author_name', 'description', 'category']
    ordering_fields = ['name', 'author_name', 'category']
