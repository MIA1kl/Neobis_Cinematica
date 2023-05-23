from django.contrib import admin

from .models import Movie, Cinema, Showtime, Room, Seat

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Showtime)
admin.site.register(Room)
admin.site.register(Seat)


