from django.shortcuts import render, redirect
from .forms import BookingsForm

# Create your views here.
def travel_booking_form(request):
    if request.method == 'POST': 
        form = BookingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Fix the redirect here
    else:
        form = BookingsForm()
    return render(request, 'booking_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
