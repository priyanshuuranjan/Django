from django.db import models

# Create your models here.

class Applicant(models.Model):
  full_name=models.CharField(max_length=100)
  email=models.EmailField()
  phone_number=models.IntegerField(max_length=10)
  address=models.TextField()
  
  
class Education(models.Model):
  degree=models.CharField(max_length=100)
  institution=models.CharField(max_length=50)
  start_date=models.DateField()
  end_date=models.DateField()
  
class Experience(models.Model):
  company=models.CharField(max_length=100)
  designation=models.CharField(max_length=100)
  start_date=models.DateField()
  end_date=models.DateField()