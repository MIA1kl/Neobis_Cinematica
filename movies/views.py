from rest_framework import viewsets, generics, permissions
from .models import Movie, Cinema, Room, Seat, Showtime
from .serializers import MovieSerializer, CinemaSerializer, RoomSerializer, SeatSerializer, ShowtimeSerializer
from django.utils import timezone
from users.permissions import IsAdminOrReadOnly



class ListMovie(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(is_active=True, release_date__gte=timezone.now().date())
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly ]

class DetailMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(is_active=True, release_date__gte=timezone.now().date())
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly ]

class ListCinema(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class DetailCinema(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class ListRoom(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class DetailRoom(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class ListSeat(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class DetailSeat(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
class ListShowtime(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]

class DetailShowtime(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    

