from django import forms
from bootstrap_datepicker_plus.widgets import TimePickerInput

from shedule.models import WorkShedule


class UpdateWorkDayForm(forms.ModelForm):
    start_time = forms.TimeField(
        required=False,
        widget=TimePickerInput(
            options={
                'format': 'HH:mm',
                'showClear': True,
                "showClose": True,
                'stepping': 30,
                'enabledHours': [
                    i for i in range(6, 23)
                ]
            },
            attrs={
                'value': '8:00:00',
                'class': 'form-control',
            },
        )
    )
    end_time = forms.TimeField(
        required=False,
        widget=TimePickerInput(
            options={
                'format': 'HH:mm',
                'showClear': True,
                "showClose": True,
                'stepping': 30,
                'enabledHours': [
                    i for i in range(6, 23)
                ]
            },
            attrs={
                'value': '20:00:00',
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = WorkShedule
        fields = ('start_time', 'end_time',)
