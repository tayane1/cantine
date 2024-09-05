from django import forms
from .models import Plat




class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['name', 'summary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }