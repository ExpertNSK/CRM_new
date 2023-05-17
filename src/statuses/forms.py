from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    status = forms.CharField(
        label='Статус',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = Status
        fields = ('status',)
