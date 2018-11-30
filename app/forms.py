from django.forms import Form
from django import forms

class AddForm(Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()

class DoubleForm(Form):
    num = forms.FloatField()

class MultThree(Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()
    num3 = forms.FloatField()
