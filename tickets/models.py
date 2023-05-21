import uuid
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

class Discount(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discounts')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    payment_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)

    
def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1] 

class Ticket(models.Model):
    methods = [
        (1, 'Visa-card'),
        (2, 'Klarna'),
        (3, 'MasterCard'),
    ]
        
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    payment_method = models.CharField(max_length=100, choices=methods, default=methods[1])
    purchase_date = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    

    
    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()
        if (
                self.ticket_type.name == "adult" or
                self.ticket_type.name == "child" or
                self.ticket_type.name == "student" and
                self.seat.room.format.name == 'small' or
                self.seat.room.format.name == 'middle' or
                self.seat.room.format.name == 'big' 
        ):
            self.price = self.ticket_type.price + \
                         self.seats.rooms.format.price
        super(Ticket, self).save(*args, **kwargs)
        

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

