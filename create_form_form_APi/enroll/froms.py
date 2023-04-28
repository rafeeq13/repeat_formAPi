from django import forms
class Student (forms.Form):
    name=forms.CharField()
    father_name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()

