from django.urls import path
from .views import (
    ListCinema,
    DetailCinema,
    ListMovie,
    DetailMovie,
    ListRoom,
    DetailRoom,
    ListSeat,
    DetailSeat,
    ListShowtime,
    DetailShowtime, 
)

app_name = 'movies'

urlpatterns = [
    path('movies/', ListMovie.as_view(), name='movie-list'),
    path('movies/<int:pk>/', DetailMovie.as_view(), name='movie-detail'),
    
    path('cinemas/', ListCinema.as_view(), name='cinema-list'),
    path('cinemas/<int:pk>/', DetailCinema.as_view(), name='cinema-detail'),
    
    path('rooms/', ListRoom.as_view(), name='room-list'),
    path('rooms/<int:pk>/', DetailRoom.as_view(), name='room-detail'),
    
    path('seats/', ListSeat.as_view(), name='seat-list'),
    path('seats/<int:pk>/', DetailSeat.as_view(), name='seat-detail'),
    
    path('showtimes/', ListShowtime.as_view(), name='showtime-list'),
    path('showtimes/<int:pk>/', DetailShowtime.as_view(), name='showtime-detail'),    
]