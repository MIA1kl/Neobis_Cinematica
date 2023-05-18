from django.db import models


from movies.models import (
    Movie,
    Cinema,
    Showtime,
)
from users.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='rooms')
    seats_available = models.IntegerField()

class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)

class PurchaseHistory(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='purchase_history')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='purchase_history')
    purchase_date = models.DateTimeField(auto_now_add=True)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)

class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Discount(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discounts')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)