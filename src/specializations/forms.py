from django import forms

from .models import Specialization




class SpecializationForm(forms.ModelForm):
    specialization = forms.CharField(
        label='Специализация',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = Specialization
        fields = ('specialization',)
