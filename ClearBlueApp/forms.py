# Forms.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django import forms
from message_strings import invalid_ph, invalid_value


class PoolChemicalTest(forms.Form):
    ph = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0, required=False,
                               error_messages={'invalid': (invalid_ph,)})
    acid_demand = forms.DecimalField(max_digits=3, decimal_places=0, min_value=0,required=False,
                               error_messages={'invalid': (invalid_value,)})
    chlorine_level = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0,required=False,
                               error_messages={'invalid': (invalid_value,)})
    bromine_level = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0,required=False,
                               error_messages={'invalid': (invalid_value,)})
    alkalinity = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0,required=False,
                               error_messages={'invalid': (invalid_value,)})
    hardness = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0,required=False,
                               error_messages={'invalid': (invalid_value,)})

    description = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
