from django import forms

class FeedbackForm(forms.Form):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    SATISFACTION_CHOICES = [('yes', 'Yes'), ('no', 'No')]
    DEPARTMENT_CHOICES = [('sales', 'Sales'), ('product', 'Product'), ('Human Resource', 'HR')]
    TOPIC_CHOICES = [('website', 'Website'), ('pricing', 'Pricing'), ('customer_service', 'Customer Service')]
    
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    rating = forms.ChoiceField(label='Rating', choices=RATING_CHOICES, widget=forms.RadioSelect)
    comment = forms.CharField(label='Comments', widget=forms.Textarea)
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES, widget=forms.Select)
    topics = forms.MultipleChoiceField(label='Feedback Topic', choices=TOPIC_CHOICES, widget=forms.CheckboxSelectMultiple)
    satisfied = forms.ChoiceField(label='Are You Satisfied', choices=SATISFACTION_CHOICES, widget=forms.RadioSelect)
    additional_info = forms.CharField(label='Additional Information', widget=forms.Textarea, required=False)  # Assuming it might be optional.

