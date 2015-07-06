# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from myauth.models import UserProfile
from myauth.forms import RegistrationForm, LoginForm, DivErrorList
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def user_register(request):
    args = {}
    args['success'] = True
    #args.update(csrf(request))
    if request.method == 'POST':
        # username = request.POST.get('username', '')
        # email = request.POST.get('email', '')
        # password = request.POST.get('password', '')
        post_data = json.loads(request.body)
        username = post_data.get(u'username', False)
        email = post_data.get(u'email', False)
        password = post_data.get(u'password', False)
        # username = request.POST.get('username', False)
        # email = request.POST.get('email', False)
        # password = request.POST.get('password', False)
        if User.objects.filter(username=username).count():
            args['success'] = False
            args['usernameErr'] = u'Пользователь с таким именем уже существует'

        if User.objects.filter(email=email).count():
            args['success'] = False
            args['emailErr'] = u'Данный email уже занят'

        if args['success']:
            user = User.objects.create_user(username, email, password);
            user.is_active = False
            user.save();
            # для python 3
            # email_hash = hashlib.sha1(email.encode()).hexdigest()[:5]
            # salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
            # activation_key = hashlib.sha1(bytes(salt + email_hash, 'ascii')).hexdigest()
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            new_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()

            email_subject = u'Подтверждение регистрации'
            email_body = u"<h2>Здравствуйте %s</h2>" \
                         u"<h3>Вы зарегистрировались на портале <a href='http://ondrive.by'>ondrive.by</a></h3> " \
                         u"<p>для подтверждения регистрации перейдите по  <a href='http://localhost:8000/auth/registration/%s'>ссылке</a></p>" \
                         u"<p>Если вы не имеете понятия о чем идет речь, просто проигнорируйте это письмо!</p>" % (username, activation_key)

            send_mail(email_subject, email_body, 'ondrive.by@gmail.com',
                      [email], fail_silently=False, html_message=email_body)
            args['resultMess'] = u'Регистрация прошла успешно'
            args['resultSubMess'] = u'инструкция по активации аккаунта выслава на email указанный при регистрации (%s)' % (email)
            args = json.dumps(args)
            return HttpResponse(args)
        else:
            args = json.dumps(args)
            return HttpResponse(args)
    return render_to_response('myauth/register.html', context_instance=RequestContext(request))


def user_confirm(request, activation_key):
    args = {}
    args['success'] = True

    if request.user.is_authenticated():
        args['success'] = False
        args['message'] = 'вы уже авторизованы'
        args['subMessage'] = 'Выйдите из своего аккаунта и попробуйте снова'
        return render_to_response('myauth/success.html', args)

    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    if user_profile.key_expires < timezone.now():
        args['success'] = False
        args['message'] = 'Невозможно подтвердить аккаунт'
        args['subMessage'] = 'время действия ссылки истекло'
        return render_to_response('myauth/success.html', args)

    user = user_profile.user
    user.is_active = True
    user.save()
    args['message'] = 'Спасибо за регистрацию'
    args['subMessage'] = 'ваш аккаунт подтвержден'
    return render_to_response('myauth/success.html', args)

@ensure_csrf_cookie
def user_login(request):
    args = {'status': False}

    if request.method == 'POST':
        post_data = json.loads(request.body)
        #username = request.POST['username']
        #password = request.POST['password']
        username = post_data.get(u'username')
        password = post_data.get(u'password')
        if User.objects.filter(username=username).count() or User.objects.filter(email=username).count():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    args['status'] = True
                    args['mess'] = "Вы авторизованы"
                else:
                    args['mess'] = 'Аккаунт заблокирован. Обратитесь к администрации'
            else:
                args['mess'] = 'Имя пользователя или пароль неверны'
        else:
            args['mess'] = 'Имя пользователя или пароль неверны'
        return HttpResponse(json.dumps(args))

    return render(request, 'myauth/login.html',
                  context_instance=RequestContext(request))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_board(request):
    args = {}
    user_id = User.objects.get(username=request.user).id
    args['user_profile'] = UserProfile.objects.get(user=user_id)
    args['user'] = request.user
    article = AutoService.objects.get(name=u'СТО Шанссервис Серова')
    form = ArticleForm(instance=article)
    args['form'] = form
    return render_to_response('myauth/userboard.html', args)

from django import forms
from service.models import *
from django.forms import ModelForm
from django import forms
class ArticleForm(ModelForm):
    specialization = forms.ModelMultipleChoiceField(
        queryset=SpecializationWork.objects.all(),
        widget=forms.CheckboxSelectMultiple(


            )
        )
    # first_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'wform__input', 'placeholder': 'Имя пользователя', 'required': 'required','ng-model':'username'}))
    class Meta:
        model = AutoService
        fields = ['name','specialization']
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
          self.fields['specialization'].initial = self.instance.specialization_work.all()