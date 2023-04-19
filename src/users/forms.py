from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import check_password

from .models import CustomUser, USER_ROLE_CHOICE


class CustomAuthenticationForm(forms.Form):
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-mask': '+7 (000) 000-00-00',
                'placeholder': 'Введите номер телефона'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            }
        )
    )

    def clean(self, *args, **kwargs):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        if phone and password:
            user = CustomUser.objects.filter(phone=phone)
            if not user.exists():
                raise forms.ValidationError('Данный номер телефона не зарегистрирован!')
            if not check_password(password, user[0].password):
                raise forms.ValidationError('Неверный пароль!')
            user = authenticate(phone=phone, password=password)
            if not user or user.is_new:
                raise forms.ValidationError('Данный пользователь неактивен. Обратитесь к администратору.')
        return super().clean(*args, **kwargs)


class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }
        )
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-mask': '+7 (000) 000-00-00',
                'placeholder': 'Введите номер телефона'
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль'
            }
        )
    )
    
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'last_name', 'first_name',
            'middle_name', 'email', 'phone'
        )
    
    def clean(self, *args, **kwargs):
        phone = self.cleaned_data.get('phone')
        if phone and len(phone) < 18:
            raise forms.ValidationError('Неверный формат номера телефона!')
        return super().clean(*args, **kwargs)


class CustomUserEditForm(UserChangeForm):
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }
        )
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'data-mask': '+7 (000) 000-00-00',
                'placeholder': 'Введите номер телефона'
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail'
            }
        )
    )
    role = forms.CharField(
        label='Должность',
        max_length=30,
        widget=forms.Select(
            choices=USER_ROLE_CHOICE,
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = (
            'last_name', 'first_name', 'middle_name',
            'email', 'phone', 'role',
        )
