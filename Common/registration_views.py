# registration_views.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from CaracalApp.views.views import render_action_template
from CaracalApp.services import create_seller

from ClearBlueApp.services import create_customer

from Common.forms import RegistrationForm, LoginForm
from Common.view_helpers import render_template
from Common.message_strings import section_registration_compete

from django.http import HttpResponseRedirect
from django.contrib import auth



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
            create_customer(new_user)  # TODO: We create a user in both TZ and CB, should only be the one they register for
            current_section = section_registration_compete
            action_template = "Auth_Auth/RegistrationThankYou.htm"
            return render_action_template(request, locals())
    else:
        form = RegistrationForm()

    return render_template(request, 'Auth_Auth/RegisterPage.html', locals())

