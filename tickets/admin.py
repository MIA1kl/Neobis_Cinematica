from django.contrib import admin
from .models import Ticket, Discount, Booking, PurchaseHistory, Feedback

admin.site.register(Ticket)
admin.site.register(Discount)
admin.site.register(Booking)
admin.site.register(PurchaseHistory)
admin.site.register(Feedback)



