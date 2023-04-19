from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from loaders.models import AREA_OF_RESIDENTS, Loader, PayMethod, PayMethodList, Specialization, Passport, Status
from users.models import CustomUser


class CreateLoaderForm(forms.ModelForm):
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию',
          }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя',
          }
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите отчество',
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
          'placeholder': 'Оставьте пустым если номера совпадают'
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
                'class': 'form-control'
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
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Status
        fields = ('status',)


class CreatePassportForm(forms.ModelForm):
    serial_number = forms.CharField(
        label='Серия номер',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'data-mask': '00 00 000000',
            'placeholder': 'XX XX XXXXXX'
        }
        )
    )
    issued_by = forms.CharField(
        label='Кем выдан',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    division_code = forms.CharField(
        label='Код подразделения',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-mask': '000-000',
                'placeholder': 'XXX-XXX'
            }
        )
    )
    date_of_issue = forms.DateField(
        label='Дата выдачи',
        widget=DatePickerInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию',
          }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя',
          }
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Введите отчество',
          }
        )
    )
    birthday = forms.DateField(
        label='День рождения',
        widget=DatePickerInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    place_of_birth = forms.CharField(
        label='Место рождения',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
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


class CreatePayMethodList(forms.ModelForm):
    pay_method = forms.CharField(
        label='Способ оплаты',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = PayMethodList
        fields = ('pay_method', )


class CreatePayMethodForm(forms.ModelForm):
    pay_method = forms.ModelChoiceField(
        label='Способ оплаты',
        queryset=PayMethodList.objects.all(),
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
            }
        )
    )
    bank = forms.CharField(
        label='Наименование банка',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    comments = forms.CharField(
        label='Комментарии к оплате',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = PayMethod
        fields = ('pay_method', 'requisites', 'bank', 'comments', )
