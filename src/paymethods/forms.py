from django import forms

from .models import PayMethod, PaymentType


class CreatePaymentType(forms.ModelForm):
    payment_type = forms.CharField(
        label='Способ оплаты',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = PaymentType
        fields = ('pay_method', )


class CreatePayMethodForm(forms.ModelForm):
    pay_method = forms.ModelChoiceField(
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
        fields = ('pay_method', 'requisites', 'bank', 'comments', )

