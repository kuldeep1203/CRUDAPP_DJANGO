from django import forms
from .models import Health

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = [ 'health_condition', 'treatment', 'past_treatments', 'past_diseases']
        labels = {
            
            'health_condition': 'Health Condition',
            'treatment': 'Treatment',
            'past_treatments': 'Past Treatments',
            'past_diseases': 'Past Diseases',
        }
        widgets = {
           
            'health_condition': forms.TextInput(attrs={'class': 'form-control',"required":False}),
            'treatment': forms.TextInput(attrs={'class': 'form-control',"required":False}),
            'past_treatments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,"required":False}),
            'past_diseases': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,"required":False}),
        }
