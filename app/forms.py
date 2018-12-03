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

class Earnings(Form):
    num1 = forms.IntegerField(min_value=0)
    num2 = forms.IntegerField(min_value=0)
    num3 = forms.IntegerField(min_value=0)

class Both(Form):
    bool1 = forms.BooleanField(required=False)
    bool2 = forms.BooleanField(required=False)

class WalkOrDrive(Form):
    num = forms.FloatField(min_value=0)
    bool = forms.BooleanField(required=False)

class HowPopulated(Form):
    num1 = forms.IntegerField(min_value=0)
    num2 = forms.FloatField(min_value=0)

class GoldStars(Form):
    num = forms.IntegerField(min_value=0)

class HowManyPoints(Form):
    num = forms.IntegerField(min_value=0)
