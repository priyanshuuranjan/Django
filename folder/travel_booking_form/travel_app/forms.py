from django import forms
from .models import Bookings

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'  # or specify the fields you want to include
