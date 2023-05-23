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
    OrderItemCreateAPIView
)

app_name = 'tickets'

urlpatterns = [
    path('books/', ListBooking.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailBooking.as_view(), name='book-detail'),
    
    path('discounts/', ListDiscount.as_view(), name='discount-list'),
    path('discounts/<int:pk>/', DetailDiscount.as_view(), name='discount-detail'),
    
    path('feedbacks/', ListFeedback.as_view(), name='feedback-list'),
    path('feedbacks/<int:pk>/', DetailFeedback.as_view(), name='feedback-detail'),
    
    path('tickets/', ListTicket.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', DetailTicket.as_view(), name='ticket-detail'),
    
    path('history/', ListPurchaseHistory.as_view(), name='history-list'),  
    
    path('order-item/', OrderItemCreateAPIView.as_view(), name='order-item'),
]