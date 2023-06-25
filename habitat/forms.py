from django import forms
from .models import habitat

class habitatinsert(forms.ModelForm):
    class Meta:
        model = habitat
        fields = ['name', 'type', 'description', 'major_fauna', 'area_covered', 'last_updated']
        labels = {
            'name': 'Name',
            'type': 'Type',
            'description': 'Description',
            'major_fauna': 'Major Fauna',
            'area_covered': 'Area Covered',
            'last_updated': 'Last Updated',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'major_fauna': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major Fauna'}),
            'area_covered': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Area Covered'}),
            'last_updated': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Last Updated'}),
        }
