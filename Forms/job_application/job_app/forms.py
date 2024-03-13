from django import forms
from .models import Applicant, Education, Experience
class ApplicantForm(forms.ModelForm):
  class Meta:
    model=Applicant
    fields=['full_name', 'email', 'phone_number', 'address']
    
class EducationForm(forms.ModelForm):
  class Meta:
    model=Education
    fields=['degree', 'institution', 'start_date', 'end_date']
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields=['company','designation','start_date','end_date']
        start_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
        end_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))