from django.urls import path
from .import views
urlpatterns = [
    path("", views.travel_booking_form, name="travel_booking_form"),
    path("", views.success, name="success"),
]