from django import forms

from loaders.models import AREA_OF_RESIDENTS, Loader, Specialization, Status
from users.models import CustomUser


class CreateLoaderForm(forms.ModelForm):
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
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
        attrs={
          'class': 'form-control',
          'data-mask': '+7 (000) 000-00-00',
          'placeholder': 'Введите номер телефона',
          'autocomplete': 'off'
        }
        )
    )
    whatsapp = forms.CharField(
        label='WhatsApp',
        required=False,
        widget=forms.TextInput(
        attrs={
          'class': 'form-control',
          'data-mask': '+7 (000) 000-00-00',
          'placeholder': 'Оставьте пустым если номера совпадают',
          'autocomplete': 'off'
        }
        )
    )
    photo = forms.ImageField(
        label='Фотография',
        required=False,
        widget=forms.FileInput(
          attrs={
            'class': 'form-control',
            'placeholder': 'Выберите фотографию',
          }
        )
    )
    area = forms.CharField(
        label='Район проживания',
        max_length=50,
        widget=forms.Select(
          choices=AREA_OF_RESIDENTS,
          attrs={
            'class': 'form-control'
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
    status = forms.ModelChoiceField(
        label='Статус',
        queryset=Status.objects.all(),
        widget=forms.Select(
          attrs={
            'class': 'form-control'
          }
        )
    )
    referer = forms.ModelChoiceField(
        label='Пригласил',
        required=False,
        queryset=CustomUser.objects.all(),
        widget=forms.Select(
          attrs={
            'class': 'form-control'
          }
        )
    )
    
    class Meta:
        model = Loader
        fields = (
            'last_name', 'first_name',
            'middle_name', 'phone',
            'whatsapp', 'specialization',
            'photo', 'area', 'status',
            'referer'
        )
    
    def clean(self, *args, **kwargs):
        phone = self.cleaned_data.get('phone')
        whatsapp = self.cleaned_data.get('whatsapp')
        if phone and len(phone) < 18:
            raise forms.ValidationError('Неверный формат номера телефона!')
        if whatsapp and len(whatsapp) < 18:
            raise forms.ValidationError('Неверный формат номера телефона!')
        return super().clean(*args, **kwargs)


class CreateSpecializationForm(forms.ModelForm):
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


class CreateStatusForm(forms.ModelForm):
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
