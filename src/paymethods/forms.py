from django import forms

from .models import PayMethod, PaymentType


class PaymentTypeForm(forms.ModelForm):
    payment_type = forms.CharField(
        label='Способ оплаты',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'id': 'payment_type'
            }
        )
    )

    class Meta:
        model = PaymentType
        fields = ('payment_type', )


class PayMethodForm(forms.ModelForm):
    payment_type = forms.ModelChoiceField(
        label='Способ оплаты',
        queryset=PaymentType.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    requisites = forms.CharField(
        label='Реквизиты для оплаты',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    bank = forms.CharField(
        label='Наименование банка',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    comments = forms.CharField(
        label='Комментарии к оплате',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = PayMethod
        fields = ('payment_type', 'requisites', 'bank', 'comments', )

