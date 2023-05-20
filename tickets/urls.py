from django.urls import path

from .views import (
    ListBooking,
    DetailBooking,
    ListDiscount,
    DetailDiscount,
    ListFeedback,
    DetailFeedback,
    ListPurchaseHistory,
    ListTicket,
    DetailTicket,
    ListTicketType,
    DetailTicketType,
)

app_name = 'tickets'

urlpatterns = [
    path('books/', ListBooking.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('books/<int:pk>/', DetailBooking.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='book-detail'),
    
    path('discounts/', ListDiscount.as_view({'get': 'list', 'post': 'create'}), name='discount-list'),
    path('discounts/<int:pk>/', DetailDiscount.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='discount-detail'),
    
    path('feedbacks/', ListFeedback.as_view({'get': 'list', 'post': 'create'}), name='feedback-list'),
    path('feedbacks/<int:pk>/', DetailFeedback.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='feedback-detail'),
    
    path('tickets/', ListTicket.as_view({'get': 'list', 'post': 'create'}), name='ticket-list'),
    path('tickets/<int:pk>/', DetailTicket.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='ticket-detail'),
    
    path('ticket-types/', ListTicketType.as_view({'get': 'list', 'post': 'create'}), name='ticket-type-list'),
    path('ticket-types/<int:pk>/', DetailTicketType.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='ticket-type-detail'),
    
    path('history/', ListPurchaseHistory.as_view({'get': 'list', 'post': 'create'}), name='history-list'),  
]