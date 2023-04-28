from django import forms
from django.core import validators

class Student(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput,label="password(again)")
    def clean(self):
        cleaned_data=super().clean()
        pwd=self.cleaned_data['password']
        rpwd=self.cleaned_data['rpassword']
        if pwd!=rpwd:
            raise forms.ValidationError('enter your password again')
        
        
    


          