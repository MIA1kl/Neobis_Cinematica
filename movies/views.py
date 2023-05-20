from rest_framework import viewsets, generics, permissions
from .models import Movie, Cinema, Genre, Room, RoomFormat, MovieFormat, Seat, Showtime
from .serializers import MovieSerializer, CinemaSerializer, GenreSerializer, RoomSerializer, RoomFormatSerializer, MovieFormatSerializer, SeatSerializer, ShowtimeSerializer
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailCinema(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListRoom(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailRoom(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListSeat(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailSeat(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ListShowtime(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailShowtime(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ListGenre(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class DetailGenre(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ListRoomsFormat(generics.ListCreateAPIView):
    serializer_class = RoomFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomFormat.objects.all()


class DetailRoomsFormat(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomFormat.objects.all()


class ListMovieFormat(generics.ListCreateAPIView):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = MovieFormat.objects.all()


class DetailMovieFormat(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = MovieFormat.objects.all()
