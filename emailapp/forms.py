from django import forms
from .models import *

class CustomForm(forms.Form):
    status = forms.CharField()
    message = forms.CharField()
    subject = forms.CharField()
    
