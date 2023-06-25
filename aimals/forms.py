from django import forms
from .models import animals
from habitat.models import habitat
class animalsinsert(forms.ModelForm):
    class Meta:
        model = animals
        #= ('age',)
        fields = ( 'aname', 'sex', 'dob','age' ,'specices', 'date_of_death' ,'date_of_arrival', 'description', 'Habitat_id', 'last_updated')
        labels = {
           
            'aname': 'Animal Name',
            'sex': 'Sex',
            'dob': 'YYYY-MM-DD',
            'age': 'Age',
            'specices': 'Species',
            'date_of_death':'Date_of_death',
            'date_of_arrival': 'Date of Arrival',
            'description': 'Description',
            'Habitat_id': 'habitat',
            'last_updated': 'Last Updated',
        }
        widgets = {
            
            'aname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'sex': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sex'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'specices': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Species'}),
            'date_of_death': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Death',"required":False}),
            'date_of_arrival': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Arrival'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',"required":False}),
            'Habitat_id': forms.Select(attrs={'class': 'form-select', 'placeholder': 'habitat'}),
            'last_updated': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Last Updated'}),
        }

