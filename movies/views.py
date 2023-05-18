from rest_framework import viewsets, decorators
from .models import Movie, Cinema
from .serializers import MovieSerializer, CinemaSerializer
from django.utils import timezone
from users.permissions import IsAdminOrReadOnly



# @decorators.action(detail=False, methods=['post'])
# def hide_movies(self, request):
#     movie_ids = request.data.get('movie_ids', [])
#     movies = Movie.objects.filter(pk__in=movie_ids)
#     movies.update(is_active=False)
#     return Response({'message': 'Movies hidden successfully.'})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True, release_date__gte=timezone.now().date())
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly ]
    
    # def get_queryset(self):
    #     # Include inactive movies for administrators
    #     if self.request.user.is_staff or self.request.users.is_admin:
    #         return Movie.objects.all()
    #     return super().get_queryset()
    
    # hide_movies = hide_movies




class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
