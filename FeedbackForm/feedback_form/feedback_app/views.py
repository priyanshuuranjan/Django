from django.shortcuts import redirect
from django.shortcuts import render
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})

def success(request):
    return render(request, 'success_sent.html')
