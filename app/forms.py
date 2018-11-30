from django.forms import Form
from django import forms

class AddForm(Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()
    
