from django import forms
from django.core import validators

class Student(forms.Form):
    error_css_class="error"
    required_css_class="required"
    name=forms.CharField(error_messages={'required':'Enter Your name!'})
    email=forms.EmailField(error_messages={'required':'Enter Your email!'})
    address=forms.CharField(error_messages={'required':'Enter Your address'})
        
        
    


          