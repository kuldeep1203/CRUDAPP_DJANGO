from django import forms
from .models import Lineage

class LineageForm(forms.ModelForm):
    class Meta:
        model = Lineage
        fields = [ 'offspring_names', 'parent_names']
        labels = {
            
            'offspring_names': 'Offspring Names',
            'parent_names': 'Parent Names',
        }
        widgets = {
           
            'offspring_names': forms.TextInput(attrs={'class': 'form-control',"required":False}),
            'parent_names': forms.TextInput(attrs={'class': 'form-control',"required":False}),
        }
