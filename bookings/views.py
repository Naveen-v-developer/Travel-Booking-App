from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from travels.models import TravelOption

@login_required
def booking_create_view(request, travel_id):
    travel = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, travel_option=travel)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel
            booking.total_price = travel.price * booking.number_of_seats
            booking.status = 'Confirmed'
            booking.save()
            travel.available_seats -= booking.number_of_seats
            travel.save()
            messages.success(request, 'Booking confirmed!')
            return redirect('bookings:booking_detail', booking.booking_id)
    else:
        form = BookingForm(travel_option=travel)
    return render(request, 'bookings/booking_form.html', {'form': form, 'travel': travel})

@login_required
def booking_list_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail_view(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def booking_cancel_view(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status == 'Cancelled':
        messages.info(request, 'Booking already cancelled.')
        return redirect('bookings:booking_detail', booking_id)
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        # Restore seats
        travel = booking.travel_option
        travel.available_seats += booking.number_of_seats
        travel.save()
        messages.success(request, 'Booking cancelled.')
        return redirect('bookings:booking_detail', booking_id)
    return render(request, 'bookings/booking_cancel.html', {'booking': booking})
