from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['plat']
        widgets = {
            'plat': forms.Select(attrs={'class': 'form-control'}),
        }