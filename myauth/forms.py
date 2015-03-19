from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'wform__input', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'wform__input', 'placeholder': 'Ваш email'}), error_messages={'invalid': 'Введите корректный email'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'wform__input', 'placeholder': 'Ваш пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'wform__input', 'name':'password2', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Введенный email уже используется!")
        return email

    def clean(self):
        password = self.cleaned_data.get('password', None)
        cpassword = self.cleaned_data.get('password2', None)
        if password and cpassword and (password == cpassword):
            return self.cleaned_data
        else:
            raise forms.ValidationError("Пароли не совпадают")



class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}), error_messages={'invalid': 'Введите корректный email'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="text-danger">%s</div>' % e for e in self])

