


from django.urls import path
from . import views

urlpatterns = [  # Corrected variable name here
    path('feedback-form/', views.feedback_form, name='feedbackform'),
    path('success/', views.success, name='success'),
]
