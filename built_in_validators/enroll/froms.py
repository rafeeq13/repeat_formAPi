from django import forms
from django.core import validators
class Student(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(4)])
    email=forms.EmailField(validators=[validators.MaxLengthValidator(10)])
    address=forms.CharField(validators=[validators.MaxLengthValidator(10)])
    password=forms.CharField(validators=[validators.MaxLengthValidator(10)])

          