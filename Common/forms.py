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

    def clean_username(self):
        # We want case insensitivity, so use the case-insensitive lookup
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username__iexact=username)
        except User.DoesNotExist:
            return username
        # Let upper level throw exception in is_valid()
        self._errors["username"] = self.error_class([self.error_messages['duplicate_username']],)


    class Meta:
        model = User
        fields = ("username", "email", )

# Create my own RegisterForm to get the email
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)