from rest_framework import serializers
from .models import  TicketType, Ticket, PurchaseHistory, Feedback, Discount, Booking
from movies.models import SeatFormat, RoomFormat



class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(required=False, allow_null=True, read_only=True)
    total_price = serializers.SerializerMethodField('calculate_total_price')

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_price', 'discount']

    
    def calculate_total_price(self, instance):
        total_price = 0
        for booking in instance.bookings.all():
            self.total_price += (self.booking.ticket_type.price + self.booking.room.room_format.price)        
        # if discount:
        #     discount_percentage = discount.percentage
        #     total_price -= (total_price * discount_percentage) / 100

        return total_price
            
class TicketSerializer(serializers.ModelSerializer):
    book = BookingSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        fields = ['payment_method', 'purchase_date', 'booking', 'book', 'total_price']
    def get_total_price(self, obj):
        return obj.booking.total_price
        

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


