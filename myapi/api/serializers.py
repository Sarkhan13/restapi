from rest_framework import serializers
from myapi.models import Post


class Postserializers(serializers.ModelSerializer):
    timesince_field = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id','date']
        # exclude = ['title']

    def get_timesince_field(self,obj):
        pass

    
    # object level validate
    def validate(self,data): 
        if data['title'] == data['text']:
            raise serializers.ValidationError('basliq ve metn eyni ola bilmez')
        
        if len(data['title']) > 5:
            raise serializers.ValidationError('basliq hedden artiq uzundur!')
        
        return data
    # field level validate
    def validate_views(self, views):
        if views > 1000000:
            raise serializers.ValidationError('Views sayi hedden artiq coxdur')
        
        if views < 0:
            raise serializers.ValidationError('Views sayi menfi ola bilmez')


# class Postserializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title= serializers.CharField()
#     text = serializers.CharField()
#     active = serializers.BooleanField()
#     views=serializers.IntegerField()
#     date= serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
    
