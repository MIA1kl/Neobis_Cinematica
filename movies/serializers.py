from rest_framework import serializers
from .models import Movie, Cinema, MovieCinema


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Cinema
        fields = '__all__'

    def get_movies(self, obj):
        movie_cinemas = MovieCinema.objects.filter(cinema=obj)
        movie_serializer = MovieSerializer(movie_cinemas.values('movie'), many=True)
        return movie_serializer.data


class MovieCinemaSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    cinema = CinemaSerializer()

    class Meta:
        model = MovieCinema
        fields = '__all__'
