from django import forms
from django.core import validators
def number_start(value):
    if value[0]!="s":
        raise forms.ValidationError('please enter your CNIC Number with - dashes!')
class Student(forms.Form):
    name=forms.CharField(validators=[number_start],max_length=11,min_length=11)
    email=forms.EmailField(validators=[validators.MaxLengthValidator(10)])
    address=forms.CharField(validators=[validators.MaxLengthValidator(10)])
    password=forms.CharField(validators=[validators.MaxLengthValidator(10)])


          