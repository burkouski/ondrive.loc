# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from myauth.models import UserProfile
from ckeditor.widgets import CKEditorWidget
from service.models import TIME_CHOICES, WORKDAY_CHOICES
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
                                   attrs={'class': 'wform__control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'wform__control', 'placeholder': 'Ваш email'}),
                            error_messages={'invalid': 'Введите корректный email'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'wform__control', 'placeholder': 'Ваш пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'wform__control'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'wform__control'}))
    nickname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'wform__control'}))
    email = forms.CharField(show_hidden_initial=True, required=True,
                            widget=forms.EmailInput(attrs={'class': 'wform__control'}),
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

class ServiceForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'wform__control'}))
    logo = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'btn btn-warning text-uppercase', 'title': u'Выберите изображение'}))
    address = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_velcom = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_velcom2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_mts = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_mts2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_life = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_life2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_city = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    phone_city2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'wform__control'}))
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={'class': 'wform__control'}),error_messages={'invalid': 'Введите корректный email'})
    site_url = forms.CharField(required=False,widget=forms.URLInput(attrs={'class': 'wform__control'}),error_messages={'invalid': 'Введите адрес сайта в формате http://yoursite.com'})
    monday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    tuesday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    wednesday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    thursday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    friday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    saturday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))
    sunday = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=WORKDAY_CHOICES))

    work_start = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))
    work_end = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))
    break_time_start = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))
    break_time_end = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))
    holiday_time_start = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))
    holiday_time_end = forms.CharField(required=False,widget=forms.Select(attrs={'class': 'wform__control wform__control--inline'},choices=TIME_CHOICES))

    teaser = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'wform__control wform__control--textarea'}))
    full_desc = forms.CharField(required=False,widget=CKEditorWidget())


class AutoserviceForm(ServiceForm):
    specialization_work = forms.ModelMultipleChoiceField(required=False,
        queryset=SpecializationWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    repair_work = forms.ModelMultipleChoiceField(required=False,
        queryset=RepairWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    diag_work = forms.ModelMultipleChoiceField(required=False,
        queryset=DiagWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    serv_work = forms.ModelMultipleChoiceField(required=False,
        queryset=ServWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    add_work = forms.ModelMultipleChoiceField(required=False,
        queryset=AddWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    add_services = forms.ModelMultipleChoiceField(required=False,
        queryset=AddServices.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'wform__checkbox'}
        )
    )
    class Meta:
        model = AutoService
        fields = ['name','address','phone_velcom','phone_velcom2','phone_mts','phone_mts2','phone_life','phone_life2','phone_city','phone_city2','email','site_url', 'logo','monday','tuesday','wednesday','thursday',
                  'friday', 'saturday','sunday','work_start','work_end','break_time_start', 'break_time_end','holiday_time_start', 'holiday_time_end','teaser', 'full_desc']

    def __init__(self, *args, **kwargs):
        super(AutoserviceForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['specialization_work'].initial = self.instance.specialization_work.all()
            self.fields['repair_work'].initial = self.instance.repair_work.all()
            self.fields['diag_work'].initial = self.instance.diag_work.all()
            self.fields['serv_work'].initial = self.instance.serv_work.all()
            self.fields['add_work'].initial = self.instance.add_work.all()
            self.fields['add_services'].initial = self.instance.add_services.all()
            #self.fields['monday'].initial = self.instance.monday

    def save(self, commit=True):
        form = super(AutoserviceForm, self).save(commit=False)

        if commit:
            form.save()

        if form.pk:
            form.specialization_work = self.cleaned_data['specialization_work']
            form.repair_work = self.cleaned_data['repair_work']
            form.diag_work = self.cleaned_data['diag_work']
            form.serv_work = self.cleaned_data['serv_work']
            form.add_work = self.cleaned_data['add_work']
            form.add_services = self.cleaned_data['add_services']
            self.save_m2m()

        return form


class CarwashForm(ServiceForm):
    # specialization_work = forms.ModelMultipleChoiceField(required=False,
    #     queryset=SpecializationWork.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    # repair_work = forms.ModelMultipleChoiceField(required=False,
    #     queryset=RepairWork.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    # diag_work = forms.ModelMultipleChoiceField(required=False,
    #     queryset=DiagWork.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    # serv_work = forms.ModelMultipleChoiceField(required=False,
    #     queryset=ServWork.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    # add_work = forms.ModelMultipleChoiceField(required=False,
    #     queryset=AddWork.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    # add_services = forms.ModelMultipleChoiceField(required=False,
    #     queryset=AddServices.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': 'wform__checkbox'}
    #     )
    # )
    class Meta:
        model = CarWash
        fields = ['name','address','phone_velcom','phone_velcom2','phone_mts','phone_mts2','phone_life','phone_life2','phone_city','phone_city2','email','site_url', 'logo','monday','tuesday','wednesday','thursday',
                  'friday', 'saturday','sunday','work_start','work_end','break_time_start', 'break_time_end','holiday_time_start', 'holiday_time_end','teaser', 'full_desc']

    # def __init__(self, *args, **kwargs):
    #     super(AutoserviceForm, self).__init__(*args, **kwargs)
    #
    #     if self.instance and self.instance.pk:
    #         self.fields['specialization_work'].initial = self.instance.specialization_work.all()
    #         self.fields['repair_work'].initial = self.instance.repair_work.all()
    #         self.fields['diag_work'].initial = self.instance.diag_work.all()
    #         self.fields['serv_work'].initial = self.instance.serv_work.all()
    #         self.fields['add_work'].initial = self.instance.add_work.all()
    #         self.fields['add_services'].initial = self.instance.add_services.all()
    #         #self.fields['monday'].initial = self.instance.monday
    #
    # def save(self, commit=True):
    #     form = super(AutoserviceForm, self).save(commit=False)
    #
    #     if commit:
    #         form.save()
    #
    #     if form.pk:
    #         form.specialization_work = self.cleaned_data['specialization_work']
    #         form.repair_work = self.cleaned_data['repair_work']
    #         form.diag_work = self.cleaned_data['diag_work']
    #         form.serv_work = self.cleaned_data['serv_work']
    #         form.add_work = self.cleaned_data['add_work']
    #         form.add_services = self.cleaned_data['add_services']
    #         self.save_m2m()
    #
    #     return form


