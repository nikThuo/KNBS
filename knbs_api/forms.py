from django import forms
from django.forms import ModelForm

from knbs_api.models import RegisteredBirthsOccurrence


class KnbsForm(ModelForm):
    class Meta:
        model = RegisteredBirthsOccurrence
        fields = ['county', 'year', 'health_facility', 'home']

        widgets = {'county': forms.HiddenInput(),
                   'year': forms.HiddenInput(),
                   'health_facility':forms.HiddenInput(),
                   #'home':forms.HiddenInput()
                   }
        exclude = {'home'}
    # #birth_id = forms.AutoField(primary_key=True)
    # county = forms.CharField(max_length=2)
    # year = forms.CharField(max_length=50)
    # health_facility = forms.CharField(max_length=50)
    # home = forms.CharField(max_length=50)