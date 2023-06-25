from django import forms
from .models import AMigrations

class AMigrationsForm(forms.ModelForm):
    class Meta:
        model = AMigrations
        fields = ['migration_period', 'migration_from', 'migration_to', 'migration_season']
        labels = {
            
            'migration_period': 'Migration Period',
            'migration_from': 'Migration From',
            'migration_to': 'Migration To',
            'migration_season': 'Migration Season',
        }
        widgets = {
            
            'migration_period': forms.TextInput(attrs={'class': 'form-control'}),
            'migration_from': forms.TextInput(attrs={'class': 'form-control'}),
            'migration_to': forms.TextInput(attrs={'class': 'form-control'}),
            'migration_season': forms.TextInput(attrs={'class': 'form-control'}),
        }
