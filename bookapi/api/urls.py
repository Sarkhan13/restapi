
from django.urls import path
from .views import BookListCreateAPIview,BookPutdeleteAPIView

urlpatterns = [
    path('all/',BookListCreateAPIview.as_view(), name='booksapi'),
    path('<int:id>/',BookPutdeleteAPIView.as_view(), name='bookdetail'),

    
]