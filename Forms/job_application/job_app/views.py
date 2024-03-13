from django.shortcuts import render, redirect

# Create your views here.

from .forms import ApplicantForm, EducationForm, ExperienceForm
def job_application(request):
    if request.method=='POST':
        applicant_form = ApplicantForm(request.POST)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        if all((applicant_form.is_valid(), education_form.is_valid(), experience_form.is_valid())):
            applicant=applicant_form.save()
            education=education_form.save()
            education.applicant=applicant
            education.save()
            experience=education_form.save()
            experience.save()
            return redirect('success')
    else:
        applicant_form=ApplicantForm()
        education_form=EducationForm()
        experience_form=ExperienceForm()    
    return render(request, 'job_application.html',{'applicant_form':applicant_form, 'education_form':education_form,'experience_form':experience_form})

def success(request):
    return render(request, 'success.html')