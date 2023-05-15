from typing import Any, Dict
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Passport


class PassportForm(forms.ModelForm):
    serial_number = forms.CharField(
        label='Серия номер',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'data-mask': '00 00 000000',
            'placeholder': 'XX XX XXXXXX',
            'autocomplete': 'off'
        }
        )
    )
    issued_by = forms.CharField(
        label='Кем выдан',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    division_code = forms.CharField(
        label='Код подразделения',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-mask': '000-000',
                'placeholder': 'XXX-XXX',
                'autocomplete': 'off'
            }
        )
    )
    date_of_issue = forms.DateField(
        label='Дата выдачи',
        widget=DatePickerInput(
            options={
                'format': 'DD-MM-YYYY',
                'locale': 'ru',
            },
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию',
            'autocomplete': 'off'
          }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя',
            'autocomplete': 'off'
          }
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите отчество',
            'autocomplete': 'off'
          }
        )
    )
    birthday = forms.DateField(
        label='День рождения',
        widget=DatePickerInput(
            options={
                    'format': 'DD-MM-YYYY',
                    'locale': 'ru',
                },
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    place_of_birth = forms.CharField(
        label='Место рождения',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    photo_main_page = forms.ImageField(
        label='Фото главной страницы',
        widget=forms.FileInput(
          attrs={
            'class': 'form-control',
            'placeholder': 'Выберите фото',
          }
        )
    )
    photo_registration = forms.ImageField(
        label='Фото страницы регистрации',
        widget=forms.FileInput(
          attrs={
            'class': 'form-control',
            'placeholder': 'Выберите фото',
          }
        )
    )

    class Meta:
        model = Passport
        fields = (
            'serial_number', 'issued_by',
            'division_code', 'date_of_issue',
            'last_name', 'first_name',
            'middle_name', 'birthday',
            'place_of_birth', 'photo_main_page',
            'photo_registration'
        )
    
    def clean(self):
        serial_number = self.cleaned_data.get('serial_number')
        division_code = self.cleaned_data.get('division_code')
        if len(serial_number) != 12:
            raise forms.ValidationError('Неверный формат серии/номера паспорта!')
        if len(division_code) != 7:
            raise forms.ValidationError('Неверный формат кода подразделения!')
        return super().clean()