
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import (
    TicketType,
    Booking,
    Ticket,
    PurchaseHistory,
    Feedback,
    Discount,
)
from .serializers import (
    TicketTypeSerializer,
    BookingSerializer,
    TicketSerializer,
    PurchaseHistorySerializer,
    FeedbackSerializer,
    DiscountSerializer,
)

from movies.models import Seat


class ListBooking(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        showtime = booking.showtime
        seats = booking.seats.all()

        # Create tickets for the selected seats
        tickets = []
        for seat in seats:
            ticket = Ticket.objects.create(booking=booking, seat=seat, showtime=showtime)
            tickets.append(ticket)

        # Update seat status as booked
        Seat.objects.filter(id__in=[seat.id for seat in seats]).update(is_booked=True)

class DetailBooking(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class ListTicketType(generics.ListCreateAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class DetailTicketType(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()
    
class ListTicket(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class DetailTicket(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class ListPurchaseHistory(generics.ReadOnlyModelViewSet):
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
