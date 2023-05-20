from django.contrib import admin

from .models import Movie, Cinema, Showtime, Genre, Room, RoomFormat,MovieFormat, Seat

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Showtime)
admin.site.register(Genre)
admin.site.register(Room)
admin.site.register(RoomFormat)
admin.site.register(MovieFormat)
admin.site.register(Seat)

