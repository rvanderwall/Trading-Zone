__author__ = 'robertv'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from message_strings import invalid_price,invalid_hunt_words,invalid_email
from message_strings import label_email, label_hunt_words
from message_strings import help_email


class ItemForSaleForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, max_length=2000)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0,
                               error_messages={'invalid' : (invalid_price,)})

class HuntItemForm(forms.Form):
    title = forms.CharField(max_length=50)
    search_text = forms.CharField(max_length=50, label= label_hunt_words)
    email = forms.EmailField(required=True)

    def clean_search_text(self):
        search_text = self.cleaned_data['search_text']
        num_words = len(search_text.split())
        if num_words > 5:
            raise forms.ValidationError(invalid_hunt_words)
        return search_text


# Create my own RegisterForm to get the email
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = label_email, max_length=30,
            required = True,
            help_text = help_email,
            error_messages = {
            'invalid': invalid_email,})

    class Meta:
        model = User
        fields = ("username", "email", )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
