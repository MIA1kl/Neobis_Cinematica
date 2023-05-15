from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, through='MovieCinema')

    def __str__(self):
        return self.name


class MovieCinema(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Movie: {self.movie.title} - Cinema: {self.cinema.name} - Featured: {self.is_featured}"
