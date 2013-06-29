# forms.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from message_strings import label_email, help_email, invalid_email



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = label_email, max_length=30,
            required = True,
            help_text = help_email,
            error_messages = {
            'invalid': invalid_email,})

    class Meta:
        model = User
        fields = ("username", "email", )

# Create my own RegisterForm to get the email
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)