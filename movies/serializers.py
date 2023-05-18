from rest_framework import serializers
from .models import Movie, Cinema, Showtime


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
        showtimes = Showtime.objects.filter(cinema=obj)
        movie_serializer = MovieSerializer(showtimes.values('movie'), many=True)
        return movie_serializer.data


class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    cinema = CinemaSerializer()

    class Meta:
        model = Showtime
        fields = '__all__'
