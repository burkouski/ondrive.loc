from django.shortcuts import render, RequestContext, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from myauth.forms import UserForm, LoginForm, DivErrorList
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, error_class=DivErrorList)

        if user_form.is_valid():
            user_form.save()
            registered = True
            login_form = LoginForm()
            return render(request, 'myauth/register.html', {'login_form': login_form, 'registered': registered}, context_instance=RequestContext(request) )

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm(error_class=DivErrorList)

    # Render the template depending on the context.
    return render(request,
            'myauth/register.html', {'user_form': user_form, 'registered': registered}, context_instance=RequestContext(request) )


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