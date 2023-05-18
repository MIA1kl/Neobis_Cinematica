from django.db import models
from datetime import timedelta


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='SOME STRING')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    imageUrl = models.URLField(default='http://www.foo.com')
    release_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    duration = models.DurationField(default=timedelta)
    age_limit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255, blank=True, null=True)
    movies = models.ManyToManyField(Movie, through='Showtime')

    def __str__(self):
        return self.name
    
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    
    def __str__(self):
        return f"Movie: {self.movie.title} - Cinema: {self.cinema.name} - Start time: {self.start_time}"


    

