from rest_framework.views import APIView
from myapi.models import Post
from .serializers import Postserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


# class Postlistview(APIView):
#     def get(self, request):

#         posts = Post.objects.filter(active=True)
#         serializer = Postserializers(posts)
#         return Response(serializer.data)