from django.urls import path
from .views import (
    ListCinema,
    DetailCinema,
    ListGenre,
    DetailGenre,
    ListMovie,
    DetailMovie,
    ListRoom,
    DetailRoom,
    ListRoomsFormat,
    DetailRoomsFormat,
    ListSeat,
    DetailSeat,
    ListShowtime,
    DetailShowtime, 
    ListSeatFormat,
    DetailSeatFormat
)

app_name = 'movies'

urlpatterns = [
    path('movies/', ListMovie.as_view(), name='movie-list'),
    path('movies/<int:pk>/', DetailMovie.as_view(), name='movie-detail'),
    
    path('cinemas/', ListCinema.as_view(), name='cinema-list'),
    path('cinemas/<int:pk>/', DetailCinema.as_view(), name='cinema-detail'),
    
    path('genres/', ListGenre.as_view(), name='genre-list'),
    path('genres/<int:pk>/', DetailGenre.as_view(), name='genre-detail'),
    
    path('rooms/', ListRoom.as_view(), name='room-list'),
    path('rooms/<int:pk>/', DetailRoom.as_view(), name='room-detail'),
    
    path('rooms-format/', ListRoomsFormat.as_view(), name='room-format-list'),
    path('rooms-format/<int:pk>/', DetailRoomsFormat.as_view(), name='room-format-detail'),
    
    path('seats/', ListSeat.as_view(), name='seat-list'),
    path('seats/<int:pk>/', DetailSeat.as_view(), name='seat-detail'),
    
    path('seats-format/', ListSeatFormat.as_view(), name='seat-format-list'),
    path('seats-format/<int:pk>/', DetailSeatFormat.as_view(), name='seat-format-detail'),
    
    path('showtimes/', ListShowtime.as_view(), name='showtime-list'),
    path('showtimes/<int:pk>/', DetailShowtime.as_view(), name='showtime-detail'),    
]