from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, NowMovie, Comment
from .serializers import MovieListSerializer,NowMovieListSerializer, CommentListSerializer
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Count

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
        movies = Movie.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')

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
        serializer = serializer[:20]

        return Response(serializer)
    
@api_view(['GET','POST'])
def community(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)

    if request.method == 'POST':
        serializer = CommentListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        comments = Comment.objects.filter(movie_id=movie_pk)
        serializer = CommentListSerializer(comments, many = True)
        return Response(serializer.data)

def search_filter(datas, word):
    serializers  = []
    for serializer in datas:
        if word in serializer.get('title'):

            serializer = MovieListSerializer(serializer)
            serializers.append(serializer.data)
    
    return serializers

@api_view(['GET'])
def search(request, word):
    movies = Movie.objects.all() 
    print( )      
    serializers = MovieListSerializer(movies, many=True)
    serializer = search_filter(serializers.data, word)
    serializer = serializer[:100]

    return Response(serializer)

