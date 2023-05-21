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

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'showtime', 'seats', 'payment_method', 'created_at', 'total_price', 'discount']
        read_only_fields = ['total_price']

    def create(self, validated_data):
        discount_data = validated_data.pop('discount', None)
        seats = validated_data.get('seats')
        showtime = validated_data.get('showtime')\
            
        discount = None
        if discount_data:
            discount_serializer = DiscountSerializer(data=discount_data)
            discount_serializer.is_valid(raise_exception=True)
            discount = discount_serializer.save()

        total_price = BookingSerializer.calculate_total_price(seats, discount)
        booking = Booking.objects.create(total_price=total_price, **validated_data)
        booking.seats.set(seats)

        return booking

    @staticmethod
    def calculate_total_price(seats, discount=None):
        total_price = 0
        
        for seat in seats:
            seat_price = 0 
            seat_type = seat.seat_type

            if seat_type == 'adult':
                seat_price = 10
            elif seat_type == 'child':
                seat_price = 5
            elif seat_type == 'student':
                seat_price = 7


            total_price += seat_price
            
        if discount:
            discount_percentage = discount.percentage
            total_price -= (total_price * discount_percentage) / 100

        return total_price
            


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


