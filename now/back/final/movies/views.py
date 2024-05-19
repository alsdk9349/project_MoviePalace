from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, NowMovie
from .serializers import MovieListSerializer,NowMovieListSerializer
from django.core.paginator import Paginator
from django.http import JsonResponse

@api_view(['GET'])
def recommend_list(request):
    if request.method == 'GET':
        nowmovies = NowMovie.objects.all()

        serializer = NowMovieListSerializer(nowmovies, many=True)
    return Response(serializer.data)

def detail(request):
    pass

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        paginator = Paginator(movies, 20)


        page = request.GET.get('page')
        page_movies = paginator.get_page(page)

        serializer = MovieListSerializer(page_movies, many=True)
        return Response(serializer.data)
    
def genre_filter(datas, genre_num):
    serializers  = []
    for serializer in datas:
        if str(genre_num) in serializer.get('genres'):
            serializer = MovieListSerializer(serializer)
            serializers.append(serializer.data)
    
    return serializers

    
@api_view(['GET'])
def genre_list(request, genre_pk):
    if request.method == 'GET':
        movies = Movie.objects.all()        
        serializers = MovieListSerializer(movies, many=True)
        serializer = genre_filter(serializers.data, genre_pk)
        serializer = serializer[:21]

        return Response(serializer)