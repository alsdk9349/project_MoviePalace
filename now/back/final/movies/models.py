from django.db import models
# Create your models here.
# models.py (Django)

from django.db import models
import datetime
# class Genre(models.Model):
#     name = models.CharField(max_length=50, null=False)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.DateField(null=True, default=datetime.date.today)
    vote_avg = models.FloatField()
    is_adult = models.BooleanField()
    poster_path = models.TextField(null=True)
    genres = models.CharField(max_length=255)  # CharField로 변경

    def save(self, *args, **kwargs):
        self.genres = ','.join(map(str, self.genres))  # 배열을 문자열로 변환하여 저장
        super(Movie, self).save(*args, **kwargs)

class NowMovie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.DateField(null=True, default=datetime.date.today)
    vote_avg = models.FloatField()
    is_adult = models.BooleanField()
    poster_path = models.TextField(null=True)
    genres = models.CharField(max_length=255)  # CharField로 변경

    def save(self, *args, **kwargs):
        self.genres = ','.join(map(str, self.genres))  # 배열을 문자열로 변환하여 저장
        super(NowMovie, self).save(*args, **kwargs)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=100)
    content = models.TextField(null = False)
    category = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
