from rest_framework import serializers
from .models import Movie, NowMovie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self, attrs):
        # 어떤 필드라도 비어있는지 확인
        for value in attrs.values():
            if value == '' or value is None:
                raise serializers.ValidationError("At least one field is empty")
        return attrs



class NowMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowMovie
        fields = '__all__'
        
    def validate(self, attrs):
        # 어떤 필드라도 비어있는지 확인
        for value in attrs.values():
            if value == '' or value is None:
                raise serializers.ValidationError("At least one field is empty")
        return attrs