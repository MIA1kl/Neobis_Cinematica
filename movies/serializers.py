from rest_framework import serializers
from .models import Movie, Cinema, Showtime, Genre, Room,RoomFormat,MovieFormat,Seat
from tickets.seriaizers import TicketSerializer



class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Genre 


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

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = "__all__"

class RoomFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFormat
        fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class ShowtimeSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)
    movie = MovieSerializer()
    cinema = CinemaSerializer()

    class Meta:
        model = Showtime
        fields = '__all__'
