from rest_framework.pagination import PageNumberPagination



class SmallPagePagination(PageNumberPagination):
    page_size = 5



class LargePagePagination(PageNumberPagination):
    page_size = 10