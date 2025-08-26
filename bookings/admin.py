from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_option', 'booking_date', 'number_of_seats', 'total_price', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'travel_option__source', 'travel_option__destination')
