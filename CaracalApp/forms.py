# Forms.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django import forms

from message_strings import invalid_price,invalid_hunt_words
from message_strings import label_hunt_words


class ItemForSaleForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=2000)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0,
                               error_messages={'invalid': (invalid_price,)})
    file = forms.ImageField(required=False)

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


