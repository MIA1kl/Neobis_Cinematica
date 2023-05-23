from rest_framework import serializers
from .models import Ticket, PurchaseHistory, Feedback, Discount, Booking, OrderItem
from movies.models import Seat, Room



class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
            
class TicketSerializer(serializers.ModelSerializer):
    # book = BookingSerializer(read_only=True)
    total_price = serializers.SerializerMethodField('total_sum')
    class Meta:
        model = Ticket
        fields = '__all__'
        
    def total_sum(self, instance):
        total_price = 10
        for order_ticket in instance.order_tickets.all():
            if(order_ticket.booking.ticket_type=='adult'):
                total_price+=200
            elif(order_ticket.booking.ticket_type=='student'):
                total_price+=150
            else:
                total_price+=120
                
            if(order_ticket.booking.room_format.room_format=='small'):
                total_price+=50
            elif(order_ticket.booking.room_format.room_format=='medium'):
                total_price+=60
            else:
                total_price+=70
        return total_price
        
class OrderItemSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(read_only=True)
    booking = BookingSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


