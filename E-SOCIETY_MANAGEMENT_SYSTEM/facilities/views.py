from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking


def create_booking(request):

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)
            booking.resident = request.user
            booking.save()

            return redirect('resident_dashboard')

    else:
        form = BookingForm()

    return render(request, "create_booking.html", {"form": form})


def booking_list(request):

    bookings = Booking.objects.all()

    return render(request, "booking_list.html", {"bookings": bookings})


def approve_booking(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    booking.status = "approved"
    booking.save()

    return redirect("booking_list")


def reject_booking(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    booking.status = "rejected"
    booking.save()

    return redirect("booking_list")