from django.db import models
from datetime import timedelta, timezone


class Movie(models.Model):
    choices_genre = (
      (1, 'action'),
      (2, 'adventure'),
      (3, 'comedy'),
      (4, 'drama'),
      (5, 'fantasy'),
      (6, 'horror'),
      (7, 'musicals'),
      (8, 'science fiction'),
      )
    title = models.CharField(max_length=255)
    description = models.TextField(default='SOME STRING')
    genre =  models.CharField(max_length=100, choices=choices_genre, default=choices_genre[1])
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
    schedule = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255, blank=True, null=True)
    movies = models.ManyToManyField(Movie, through='Showtime')

    def __str__(self):
        return self.name


class Room(models.Model):
    choices_room = (
      (1, 'small'),
      (2, 'medium'),
      (3, 'big'),
      )
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='rooms')
    seats_available = models.IntegerField()
    room_format = models.CharField(max_length=100, choices=choices_room, default=choices_room[1])
    

class Seat(models.Model):
    choices_seat = (
      (1, '№1'),
      (2, '№2'),
      (3, '№3'),
      (4, '№4'),
      (5, '№5'),
      (6, '№6'),
      (7, '№7'),
      (8, '№8'),
      )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats')
    is_available = models.BooleanField(default=True)
    seat_number = models.CharField(max_length=100, choices=choices_seat, default=choices_seat[1])
    
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='cinema')
    start_time = models.DateTimeField()
    
    def __str__(self):
        return f"Movie: {self.movie.title} - Cinema: {self.cinema.name} - Start time: {self.start_time}"


    

