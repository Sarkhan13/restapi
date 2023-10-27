from rest_framework import serializers
from myapi.models import Post





class Postserializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title= serializers.CharField()
    text = serializers.CharField()
    active = serializers.BooleanField()
    views=serializers.IntegerField()
    date= serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
