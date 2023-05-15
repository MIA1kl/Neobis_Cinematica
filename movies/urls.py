from django.urls import path
from .views import MovieViewSet, CinemaViewSet

app_name = 'movies'

urlpatterns = [
    path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='movie-detail'),
    path('cinemas/', CinemaViewSet.as_view({'get': 'list', 'post': 'create'}), name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='cinema-detail'),
]