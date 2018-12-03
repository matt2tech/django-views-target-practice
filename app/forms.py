from django.forms import Form
from django import forms

class AddForm(Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')

class DoubleForm(Form):
    num = forms.FloatField(label='Number')

class MultThree(Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')
    num3 = forms.FloatField(label='Number 3')

class Earnings(Form):
    num1 = forms.IntegerField(min_value=0, label='Class A Seats Sold')
    num2 = forms.IntegerField(min_value=0, label='Class B Seats Sold')
    num3 = forms.IntegerField(min_value=0, label='Class C Seats Sold')

class Both(Form):
    bool1 = forms.BooleanField(required=False, label='Boolean 1')
    bool2 = forms.BooleanField(required=False, label='Boolean 2')

class WalkOrDrive(Form):
    num = forms.FloatField(min_value=0, label='Miles')
    bool = forms.BooleanField(required=False, label='Good Weather?')

class HowPopulated(Form):
    num1 = forms.IntegerField(min_value=0, label='Population')
    num2 = forms.FloatField(min_value=0, label='Land Area')

class GoldStars(Form):
    num = forms.IntegerField(min_value=0, label='Score')

class HowManyPoints(Form):
    num = forms.IntegerField(min_value=0)
