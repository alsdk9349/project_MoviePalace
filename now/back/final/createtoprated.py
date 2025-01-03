import requests
import json
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 불러오기
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        # for movie in movies['results']:
        for movie in movies.get('results'):
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'is_adult' : movie['adult']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("top_rated.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

get_movie_datas()