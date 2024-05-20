from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.movie_list),
    path('recommend/',views.recommend_list),
    path('<int:movie_pk>/',views.detail),
    path('recommend/genred/<int:genre_pk>/', views.genre_list),
    path('<int:movie_pk>/community/',views.community),
    path('search/<str:word>/', views.search)
]
