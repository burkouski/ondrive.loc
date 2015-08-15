# -*- coding: utf-8 -*-
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail


def contacts_view(request):
    return render(request, 'contacts/contacts.html')


def cooperation_view(request):
    return render(request, 'contacts/cooperation.html')


@ensure_csrf_cookie
def send_message(request):
    args = {}
    post_data = json.loads(request.body)
    name = post_data.get(u'name', False)
    email = post_data.get(u'email', False)
    subject = post_data.get(u'subject', False)
    message = post_data.get(u'message', False)
    if not name:
        name = u'Не указано'
    if not email:
        email = u'Не указан'
    if not subject:
        subject = u'Не указана'
    # name = request.POST.get('name','')
    # email = request.POST.get('email','')
    # subject = request.POST.get('subject','')
    # message = request.POST.get('message','')
    # if not name:
    # name = 'Не указано'
    # if not email:
    #     email = 'Не указан'
    # if not subject:
    #     subject = 'Не указана'
    args['success'] = True
    html_content = u"<h3 style='color: red'>Сообщение с сайта ondrive.by</h3>" \
                   u"<span>Имя: %s</span><br/>" \
                   u"<span>Email: %s</span><br/>" \
                   u"<span>Тема: %s</span><br/>" \
                   u"<p>%s</p>" % (name, email, subject, message)
    send_mail(subject, html_content, 'info@ondrive.by', ['ondrive.by@gmail.com'], fail_silently=False,
              html_message=html_content)

    if request.method == 'POST':
        return HttpResponse(json.dumps(args))

