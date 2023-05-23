
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from users.models import User

from .models import (
    Booking,
    Ticket,
    PurchaseHistory,
    Feedback,
    Discount,
)
from .serializers import (
    BookingSerializer,
    TicketSerializer,
    PurchaseHistorySerializer,
    FeedbackSerializer,
    DiscountSerializer,
)

from movies.models import Seat


class ListBooking(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



class DetailBooking(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    
class ListTicket(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class DetailTicket(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class ListPurchaseHistory(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    
class ListFeedback(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

class DetailFeedback(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class ListDiscount(generics.ListCreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()

class DetailDiscount(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
