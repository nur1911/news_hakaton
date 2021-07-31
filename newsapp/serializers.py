from rest_framework import serializers

from newsapp.models import News_Details


class NewsDetailsListSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    class Meta:
        model = News_Details
        fields = ['title', 'image']

class NewsDetailsSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    class Meta:
        model = News_Details
        fields = ['header_title','text','add_date','image']



class NewsDetailSerializerPost(serializers.ModelSerializer):
    image = serializers.URLField()
    filter = serializers.CharField(max_length=200)
    language = serializers.CharField(max_length=200)

    class Meta:
        model = News_Details
        fields = ('__all__')


