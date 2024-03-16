from django.urls import path
from .views import travel_booking_form, success  # fix the import statement

urlpatterns = [
    path("", travel_booking_form, name="travel_booking_form"),
    path("success/", success, name="success"),
]