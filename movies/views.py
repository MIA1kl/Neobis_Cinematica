from rest_framework import viewsets
from .models import Movie, Cinema
from .serializers import MovieSerializer, CinemaSerializer
from django.utils import timezone


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True, release_date__gte=timezone.now().date())
    serializer_class = MovieSerializer


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
