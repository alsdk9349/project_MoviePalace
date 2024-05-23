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
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        # for movie in movies['results']:
        for movie in movies.get('results'):
            if movie.get('release_date', '') and not movie.get('adult', False) and movie.get('vote_count', None) is not None and movie.get('original_language', '') == 'ko':  # is_adult가 False인 경우만 추가
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'is_adult' : movie['adult'],
                    'original_language' : movie['original_language'],
                    'vote_count' : movie['vote_count'],
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.nowmovie",
                    "fields": fields
                }

                total_data.append(data)

    # vote_average를 기준으로 정렬
    total_data_sorted = sorted(total_data, key=lambda x: x['fields']['vote_count'], reverse=True)
    
    # 상위 20개의 데이터만 선택하여 JSON 파일로 저장
    top_20_data = total_data_sorted[:20]

    with open("nowplaying.json", "w", encoding="utf-8") as w:
        json.dump(top_20_data, w, ensure_ascii=False)
get_movie_datas()