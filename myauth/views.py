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
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if User.objects.filter(username=username).count():
            args['success'] = False
            args['usernameErr'] = 'Пользователь с таким именем уже существует'

        if User.objects.filter(email=email).count():
            args['success'] = False
            args['emailErr'] = 'Данный email уже занят'

        if args['success']:
            user = User.objects.create_user(username, email, password);
            user.is_active = False
            user.save();
            email_hash = hashlib.sha1(email.encode()).hexdigest()[:5]
            salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
            activation_key = hashlib.sha1(bytes(salt + email_hash, 'ascii')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            new_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()

            email_subject = 'Account confirmation'
            email_body = "<h2>Здравствуйте %s</h2>" \
                         "<h3>Вы зарегистрировались на портале <a href='http://ondrive.by'>ondrive.by</a></h3> " \
                         "<p>для подтверждения регистрации перейдите по  <a href='http://localhost:8000/auth/registration/%s'>ссылке</a></p>" \
                         "<p>Если вы не имеете понятия о чем идет речь, просто проигнорируйте это письмо!</p>" % (username, activation_key)

            send_mail(email_subject, email_body, 'burkouski.vs@gmail.com',
                      ['burkouski.vs@gmail.com'], fail_silently=False, html_message=email_body)
            args['resultMess'] = 'Регистрация прошла успешно'
            args['resultSubMess'] = 'инструкция по активации аккаунта выслава на email указанный при регистрации (%s)' % email
            args = json.dumps(args)
            return HttpResponse(args)
        else:
            args = json.dumps(args)
            return HttpResponse(args)
    return render_to_response('myauth/register.html', context_instance=RequestContext(request))


def user_login(request):
    mess = ''
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                mess = 'Аккаун заблокирован. Обратитесь к администрации'
        else:
            # Bad login details were provided. So we can't log the user in.
            mess = 'Имя пользователя или пароль неверны'

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    return render(request, 'myauth/login.html', {'login_form': login_form, 'mess': mess},
                  context_instance=RequestContext(request))


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
