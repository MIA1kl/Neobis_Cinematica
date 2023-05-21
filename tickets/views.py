
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
        Seat.objects.filter(id__in=[seat.id for seat in seats]).update(is_available=False)


class DetailBooking(generics.RetrieveUpdateDestroyAPIView):
    
    @staticmethod
    def create_booking(request):
        seats = request.data.get('seats', [])  # Assuming you receive the selected seats in the request data
        showtime = request.data.get('showtime')
        # Filter out seats that are not available
        available_seats = Seat.objects.filter(id__in=seats, is_available=True)

        if len(seats) != available_seats.count():
            # Some selected seats are not available
            return Response({'error': 'Some seats are not available.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the booking and associate the available seats
        booking = Booking.objects.create(user=request.user, showtime=showtime)
        booking.seats.set(available_seats)

        # Update the total price based on the selected seats
        booking.total_price = BookingSerializer.calculate_total_price(available_seats)
        booking.save()

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
