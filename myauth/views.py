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


def user_register(request):
    args = {}
    args.update(csrf(request))
    registered = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            email_hash = hashlib.sha1(email.encode()).hexdigest()[:5]
            salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
            activation_key = hashlib.sha1(bytes(salt+email_hash, 'ascii')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user=User.objects.get(username=username)

            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
                key_expires=key_expires)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                ['ondrive.by@gmail.com'], fail_silently=False)

            return HttpResponseRedirect('/auth/registration/success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('myauth/register.html', args, context_instance=RequestContext(request))
    # registered = False
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST, error_class=DivErrorList)
    #
    #     if user_form.is_valid():
    #         user_form.save()
    #         registered = True
    #         login_form = LoginForm()
    #         return render(request, 'myauth/register.html', {'login_form': login_form, 'registered': registered}, context_instance=RequestContext(request) )
    #
    # # Not a HTTP POST, so we render our form using two ModelForm instances.
    # # These forms will be blank, ready for user input.
    # else:
    #     user_form = UserForm(error_class=DivErrorList)
    #
    # # Render the template depending on the context.
    # return render(request,
    #         'myauth/register.html', {'user_form': user_form, 'registered': registered}, context_instance=RequestContext(request) )


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
    return render(request,'myauth/login.html', {'login_form': login_form, 'mess': mess}, context_instance=RequestContext(request) )

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')