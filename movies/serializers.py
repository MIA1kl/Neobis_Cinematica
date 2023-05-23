from rest_framework import serializers
from .models import Movie, Cinema, Showtime, Room, Seat
from tickets.serializers import TicketSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        

class SeatSerializer(serializers.ModelSerializer):
    is_available = serializers.ReadOnlyField()
    class Meta:
        model = Seat
        fields = '__all__'

class ShowtimeSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    movie = MovieSerializer()

    class Meta:
        model = Showtime
        fields = '__all__'
