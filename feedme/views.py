from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
def status_500(request, *args, **kwargs):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    response = render(request, '500.html', context)
    response.status_code = 500
    return response

def view_home(request):
    """
    Function enables user to view the home page.
    """
    return render(request, 'index.html')


def view_menu(request):
    """
    Function enables user to view menu page.
    """
    return render(request, 'menu.html')


@login_required
def make_booking(request):
    """
    Function enables user to make a booking
    and add it to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        # validation_response = validate_booking(form)
        # if not validation_response:
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'make_booking.html', context)
    
    
# def validate_booking(booking_form):
#     form = BookingForm(booking_form)
#     if form.is_valid():
#         return 'Booking date must be in the future.'
#     elif find_booking(form):
#         return 'booking already exists'

# def find_booking(form):
#     user = request.user
#     booking_date = form.booking_date
#     booking_time = form.booking_time
#     unique_booking = Booking.objects.filter(
#         user=user, booking_date=booking_date, booking_time=booking_time).exists()
#     return unique_booking
        

@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        else:
            messages.error(request, 'Booking date must be in the future.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, 'Your booking has been deleted.')
    return redirect('view_booking')



