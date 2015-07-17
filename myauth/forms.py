# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from myauth.models import UserProfile
from service.models import *


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'wform__input', 'placeholder': 'Имя пользователя', 'required': 'required',
                   'ng-model': 'username'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'wform__input', 'placeholder': 'Ваш email', 'required': 'required'}),
        error_messages={'invalid': 'Введите корректный email', 'required': 'true'})
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'wform__input', 'placeholder': 'Ваш пароль', 'required': 'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'wform__input', 'name': 'password2', 'placeholder': 'Повторите пароль',
               'required': 'required'}))

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
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
                            error_messages={'invalid': 'Введите корректный email'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(show_hidden_initial=True, required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            error_messages={'invalid': 'Введите корректный email'})
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'btn btn-warning text-uppercase', 'title': u'Выберите изображение'}))

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'nickname', 'avatar', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        # if User.objects.filter(email=email).exists():
        # raise ValidationError("Введенный email уже используется!")
        return email

    def clean(self):
        print self.initial['email']
        if self.initial['email'] != self.cleaned_data.get('email', None):
            email = self.cleaned_data.get('email', None)
            if UserProfile.objects.filter(email=email).exists():
                self._errors["email"] = ErrorList([u"Данный email занят"])


class AutoserviceForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-warning text-uppercase', 'title': u'Выберите изображение'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_velcom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_velcom2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_mts = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_mts2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_life = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_life2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_city2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}),error_messages={'invalid': 'Введите корректный email'})

    specialization = forms.ModelMultipleChoiceField(
        queryset=SpecializationWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
        )
    )
    # first_name = forms.CharField(
    # widget=forms.TextInput(attrs={'class': 'wform__input', 'placeholder': 'Имя пользователя', 'required': 'required','ng-model':'username'}))
    class Meta:
        model = AutoService
        fields = ['name','address','email','phone_velcom','phone_velcom2','phone_mts','phone_mts2','phone_life','phone_life2','phone_city','phone_city2', 'logo','monday','tuesday','wednesday','thursday',
                  'friday', 'saturday','sunday']

    def __init__(self, *args, **kwargs):
        super(AutoserviceForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['specialization'].initial = self.instance.specialization_work.all()
            #self.fields['monday'].initial = self.instance.monday

    def save(self, commit=True):
        topping = super(AutoserviceForm, self).save(commit=False)

        if commit:
            topping.save()

        if topping.pk:
            topping.specialization_work = self.cleaned_data['specialization']
            self.save_m2m()

        return topping


class DivErrorList(ErrorList):
    # def __str__(self):
    # return self.as_divs()
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="text-danger">%s</div>' % e for e in self])

