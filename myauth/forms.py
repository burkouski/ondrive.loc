# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'wform__input', 'placeholder': 'Имя пользователя', 'required': 'required','ng-model':'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'wform__input', 'placeholder': 'Ваш email', 'required': 'required'}),
                            error_messages={'invalid': 'Введите корректный email', 'required': 'true'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'wform__input', 'placeholder': 'Ваш пароль', 'required': 'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'wform__input', 'name': 'password2', 'placeholder': 'Повторите пароль', 'required': 'required'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

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

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.is_active = False
            user.save()

        return user


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
                            error_messages={'invalid': 'Введите корректный email'})
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

