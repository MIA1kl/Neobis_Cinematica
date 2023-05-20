from django.db import models


from movies.models import (
    Movie,
    Cinema,
    Showtime,
    Seat
)
from users.models import User




class TicketType(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    methods = [
        (1, 'Visa-card'),
        (2, 'Klarna'),
        (3, 'MasterCard'),
    ]
    
    def save(self, *args, **kwargs):
        if (
                self.ticket_type.name == "adult" or
                self.ticket_type.name == "child" or
                self.ticket_type.name == "student" and
                self.seats.rooms.format.name == 'small' or
                self.seats.rooms.format.name == 'middle' or
                self.seats.rooms.format.name == 'big' or
                self.seats.rooms.format.name == 'Imax'
        ):
            self.price = self.ticket_type.price + \
                         self.seats.rooms.format.price
        super().save(*args, **kwargs)


class PurchaseHistory(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='purchase_history')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='purchase_history')
    ticket_type = models.CharField(max_length=255)
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