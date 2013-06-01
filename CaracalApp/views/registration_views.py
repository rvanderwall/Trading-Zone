__author__ = 'robertv'

from django.http import HttpResponseRedirect
from django.contrib import auth

from CaracalApp.forms import RegistrationForm, LoginForm
from CaracalApp.views.view_helpers import render_template, render_action_template
from CaracalApp.services import create_seller
from CaracalApp.message_strings import section_registration_compete

#https://github.com/yourcelf/django-registration-defaults

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
        else:
            login_failed=True

    form = LoginForm()
    return render_template(request, 'Auth_Auth/LoginPage.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            create_seller(new_user)
            current_section = section_registration_compete
            action_template = "Auth_Auth/RegistrationThankYou.htm"
            return render_action_template(request, locals())
    else:
        form = RegistrationForm()

    return render_template(request, 'Auth_Auth/RegisterPage.html', locals())

