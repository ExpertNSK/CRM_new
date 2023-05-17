from django import forms

from clients.models import TYPES_CLIENTS, Client
from specializations.models import Specialization


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
                'autocomplete': 'off',
                'placeholder': 'Введите полное наименование организации'
            }
        )
    )
    short_name = forms.CharField(
        label='Краткое наименование',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Введите удобное наименование для поиска организации'
            }
        )
    )
    specialization = forms.ModelMultipleChoiceField(
        label='Вид работ для контрагента',
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
                'autocomplete': 'off',
                'placeholder': 'Введите ИНН организации',
                'data-mask': '000000000000',
            }
        )
    )
    kpp = forms.IntegerField(
        label='КПП',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Для юридических лиц',
                'data-mask': '000000000',
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
                'autocomplete': 'off',
                'placeholder': 'В случае ИП – адрес места регистрации Предпринимателя'
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
                'autocomplete': 'off',
                'placeholder': 'Оставьте пустым, если совпадает с юридическим адресом'
            }
        )
    )
    payment_account = forms.CharField(
        label='Расчетный счет организации',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'data-mask': '00000000000000000000',
            }
        )
    )
    correspondent_account = forms.CharField(
        label='Корреспондентский счет банка',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'data-mask': '00000000000000000000',
            }
        )
    )
    bik = forms.CharField(
        label='БИК банка',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'data-mask': '000000000',
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
        exclude = (
            'is_active',
        )
