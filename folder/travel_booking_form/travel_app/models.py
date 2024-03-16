from django.db import models

# Create your models here.
class Bookings(models.Model):
    DESTINATION_CHOICES = (('India','India'), ('Paris','Paris'),('France','France'),('New York','New York'))  # Destination ID
    destination = models.CharField(max_length=250,choices=DESTINATION_CHOICES) # Destination of the trip
    full_name = models.CharField(max_length=100)  # Full name of the customer
    email = models.EmailField()                
    phone = models.IntegerField(max_length=10)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    adults = models.IntegerField(default=1)   # Number of Adults in the party
    children = models.IntegerField(default=1)  # Number of Children in the party
    special_request=models.TextField(blank=True)     # Any Special Request for the Customer?
    
