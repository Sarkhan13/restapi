from bookapi.models import Book
from .serializers import Bookserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import generics
from .paginations import SmallPagePagination,LargePagePagination

class BookListCreateAPIview(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class = Bookserializer
    pagination_class = LargePagePagination


class BookPutdeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Book.objects.all()
    serializer_class = Bookserializer
    lookup_field = 'id'


# class BookListCreateAPIview(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request,*args, **kwargs)
    

#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args, **kwargs)