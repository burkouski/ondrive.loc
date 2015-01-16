from django.shortcuts import render, RequestContext
from django.contrib.auth.models import User
from myauth.forms import UserForm, DivErrorList
from django.core.exceptions import ValidationError


def register(request):
    registered = False
    mess = ''
    if request.method == 'POST':
        user_form = UserForm(request.POST, error_class=DivErrorList)

        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            email = user_form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            registered = True
            user_form = UserForm()
            mess = u'Регистрация прошла успешно! '

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm(error_class=DivErrorList)

    # Render the template depending on the context.
    return render(request,
            'myauth/register.html', {'user_form': user_form, 'mess': mess}, context_instance=RequestContext(request) )