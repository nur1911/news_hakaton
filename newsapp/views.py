from django.shortcuts import render

# Create your views here.
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from newsapp.models import News_Details
from newsapp.serializers import NewsDetailsListSerializer, NewsDetailsSerializer, NewsDetailSerializerPost


@api_view (['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':

        language_query = request.query_params.get('language')
        category_query = request.query_params.get('category')
        queryset = News_Details.objects.filter(lang__name=language_query)
        if category_query:
            queryset = News_Details.objects.filter(filter__name=category_query)
        seriliazer = NewsDetailsListSerializer(queryset, many=True)
        return Response(seriliazer.data)

    elif request.method == 'POST':
        serializer = NewsDetailSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view (['GET', 'POST'])
def news_detail(request,pk):
    if request.method == 'GET':
        queryset = News_Details.objects.get(pk=pk)
        serializer = NewsDetailsSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NewsDetailSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













