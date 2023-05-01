from django import forms

from clients.models import TYPES_CLIENTS, Client
from loaders.models import Specialization


class CreateClientForm(forms.ModelForm):
    type = forms.CharField(
        label='Тип контрагента',
        max_length=16,
        widget=forms.Select(
            choices=TYPES_CLIENTS,
            attrs={
                'class': 'form-control'
            }
        )
    )
    legal_name = forms.CharField(
        label='Юридическое наименование',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    short_name = forms.CharField(
        label='Краткое наименование',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    specialization = forms.ModelMultipleChoiceField(
        label='Специализация',
        queryset=Specialization.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
            }
        ),
    )
    inn = forms.IntegerField(
        label='ИНН',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    kpp = forms.IntegerField(
        label='КПП',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    legal_address = forms.CharField(
        label='Юридический адрес',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    actual_address = forms.CharField(
        label='Фактический адрес',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    payment_account = forms.IntegerField(
        label='Расчетный счет',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    correspondent_account = forms.IntegerField(
        label='Корреспондентский счет',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    bik = forms.IntegerField(
        label='БИК',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    bank = forms.CharField(
        label='Наименование банка',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = Client
        fields = (
            '__all__'
        )
