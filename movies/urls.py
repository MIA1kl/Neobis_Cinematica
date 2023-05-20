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
    DetailShowtime
)

app_name = 'movies'

urlpatterns = [
    path('movies/', ListMovie.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movies/<int:pk>/', DetailMovie.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='movie-detail'),
    
    path('cinemas/', ListCinema.as_view({'get': 'list', 'post': 'create'}), name='cinema-list'),
    path('cinemas/<int:pk>/', DetailCinema.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='cinema-detail'),
    
    path('genres/', ListGenre.as_view({'get': 'list', 'post': 'create'}), name='genre-list'),
    path('genres/<int:pk>/', DetailGenre.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='genre-detail'),
    
    path('rooms/', ListRoom.as_view({'get': 'list', 'post': 'create'}), name='room-list'),
    path('rooms/<int:pk>/', DetailRoom.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='room-detail'),
    
    path('rooms-format/', ListRoomsFormat.as_view({'get': 'list', 'post': 'create'}), name='room-format-list'),
    path('rooms-format/<int:pk>/', DetailRoomsFormat.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='room-format-detail'),
    
    path('seats/', ListSeat.as_view({'get': 'list', 'post': 'create'}), name='seat-list'),
    path('seats/<int:pk>/', DetailSeat.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='seat-detail'),
    
    path('showtimes/', ListShowtime.as_view({'get': 'list', 'post': 'create'}), name='showtime-list'),
    path('showtimes/<int:pk>/', DetailShowtime.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='showtime-detail'),    
]