import uuid
from django.db import models
from movies.models import (
    Movie,
    Cinema,
    Showtime,
    Seat,
    Room

)
from users.models import User


class Discount(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discounts')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Booking(models.Model):
    choices_ticket = (
      (1, 'adult'),
      (2, 'student'),
      (3, 'child'),
      )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100, choices=choices_ticket, default=choices_ticket[1])
    room_format = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)


class Ticket(models.Model):
    methods = [
        (1, 'Visa-card'),
        (2, 'Klarna'),
        (3, 'MasterCard'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    payment_method = models.CharField(max_length=100, choices=methods, default=methods[1])
    purchase_date = models.DateTimeField(auto_now_add=True)
    # booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, related_name='bookings')
    
    def __str__(self):
        return f"User: {self.booking.user} - Booking: {self.booking.showtime} - Room: {self.booking.room_format} - Seat: {self.payment_method}"
    

class OrderItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='order_tickets')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, related_name='order_bookings')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.ticket.customer} books - {self.booking.showtime}"
    
        

class PurchaseHistory(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='purchase_history')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='purchase_history')
    purchase_date = models.DateTimeField(auto_now_add=True)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)

class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='feedback', null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

