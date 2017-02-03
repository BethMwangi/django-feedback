import re
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import *

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Rewrite Password "))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class FeedbackForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    phone_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    LOCATIONS = (  
    ('NRB', 'Nairobi'),
    ('KIS', 'Kisumu'),
    ('MBS', 'Mombasa'),
    ('MACH', 'Machakos'),
    ('KIT', 'Kitui'),)

    neighbourhood = forms.MultipleChoiceField(choices = LOCATIONS, widget= forms.CharField(), label=("Neighbourhood"))
    CHOICES = (('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),)
    rating = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple(), label=_("Ratings"))


    



 