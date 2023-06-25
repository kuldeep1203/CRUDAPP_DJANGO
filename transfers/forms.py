from django import forms
from .models import Transfer

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = [ 'source', 'destination', 'reason', 'date_of_transfer']
        labels = {
         
            'source': 'Source',
            'destination': 'Destination',
            'reason': 'Reason',
            'date_of_transfer': 'Date of Transfer',
        }
        widgets = {
           
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_transfer': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        }
