
from django.urls import path
from .views import Postlistview,Postdetailview,Authorlistview

urlpatterns = [
    
    path('all/',Postlistview.as_view(), name='allapi'),
    path('<int:id>/',Postdetailview.as_view(),name='apidetail'),
    path('authors/', Authorlistview.as_view(),name='authors'),
]