from rest_framework import serializers
from .models import  TicketType, Ticket, PurchaseHistory, Feedback, Discount, Booking




class TicketSerializer(serializers.ModelSerializer):
    # seat = SeatSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'showtime', 'seats', 'payment_method', 'created_at', 'total_price']
        
    @staticmethod
    def get_total_price(obj):
        tickets = Ticket.objects.filter(orders=obj.id)
        total_price = 0
        for ticket in tickets:
            total_price += ticket.price
        return total_price


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
