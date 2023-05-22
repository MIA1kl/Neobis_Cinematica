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
    

    # def create(self, validated_data):
    #     discount_data = validated_data.pop('discount', None)
    #     seats = validated_data.get('seats')
    #     showtime = validated_data.get('showtime')
            
    #     discount = None
    #     if discount_data:
    #         discount_serializer = DiscountSerializer(data=discount_data)
    #         discount_serializer.is_valid(raise_exception=True)
    #         discount = discount_serializer.save()

    #     total_price = BookingSerializer.calculate_total_price(seats, discount)
    #     booking = Booking.objects.create(total_price=total_price, showtime=showtime)
    #     booking.seats.set(seats)

    #     return booking

    
    def calculate_total_price(self, instance):
        total_price = 0
        for booking_item in instance.booking_items.all():
            self.price += (self.booking_item.ticket_type.price + self.booking_item.seat.room.room_format.price)
        return total_price
        
        # for seat in seats:
        #     seat_price = 0 
        #     seat_format = seat.seat_type

        #     if seat_type == 'adult':
        #         seat_price = 10
        #     elif seat_type == 'child':
        #         seat_price = 5
        #     elif seat_type == 'student':
        #         seat_price = 7


            # total_price += seat_price
            
        if discount:
            discount_percentage = discount.percentage
            total_price -= (total_price * discount_percentage) / 100

        return total_price
            
class TicketSerializer(serializers.ModelSerializer):
    book = BookingSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


