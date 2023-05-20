from rest_framework import serializers
from .models import  TicketType, Ticket, PurchaseHistory, Feedback, Discount
from movies.serializers import SeatSerializer



class TicketSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

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
