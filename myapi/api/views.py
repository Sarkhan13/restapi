from rest_framework.views import APIView
from myapi.models import Post
from .serializers import Postserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404



class Postlistview(APIView):
    def get(self, request):
        posts = Post.objects.filter(active=True)
        serializer = Postserializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Postserializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
           serializer.errors ,status=status.HTTP_400_BAD_REQUEST
        )
    

class Postdetailview(APIView):
    def get_object(self, id):
        post_ins = get_object_or_404(Post, id=id)
        return post_ins

    def get(self,request,id):
        post = self.get_object(id=id)
        serializer = Postserializers(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        post = self.get_object(id=id)
        serializer = Postserializers(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
             {
                'error':{
                    'code':400,
                    'message':'Put requestde problem yarandi'
                }
            },status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self,request,id):
        post = self.get_object(id=id)
        post.delete()
        return Response(
            {
                'message':f'{id}-idli post silindi'
            }
        )
