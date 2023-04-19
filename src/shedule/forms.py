from django import forms
from bootstrap_datepicker_plus.widgets import TimePickerInput

from shedule.models import WorkShedule


class UpdateWorkDayForm(forms.ModelForm):
    start_time = forms.TimeField(
        required=False,
        widget=TimePickerInput(
            options={'format': 'HH:mm', 'showClear': True, "showClose": True,},
            attrs={
                'class': 'form-control',
            },
        )
    )
    end_time = forms.TimeField(
        required=False,
        widget=TimePickerInput(
            options={'format': 'HH:mm', 'showClear': True, "showClose": True,},
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = WorkShedule
        fields = ('start_time', 'end_time',)
