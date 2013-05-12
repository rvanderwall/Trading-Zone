__author__ = 'robertv'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ItemForSaleForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, max_length=2000)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)

class HuntItemForm(forms.Form):
    title = forms.CharField(max_length=50)
    search_text = forms.CharField(max_length=50, label='Keywords for your hunt')
    email = forms.EmailField(required=True)

    def clean_search_text(self):
        search_text = self.cleaned_data['search_text']
        num_words = len(search_text.split())
        if num_words > 5:
            raise forms.ValidationError("Please use less than 6 words to hunt.")
        return search_text


# Create my own RegisterForm to get the email
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = "Email",
            required=True,
            help_text=("Required. Must be valid email address"),
            error_messages={
            'invalid': ("Must be valid email address")})

    class Meta:
        model = User
        fields = ("username", "email", )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
