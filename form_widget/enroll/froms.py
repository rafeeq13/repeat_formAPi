from django import forms
class Student(forms.Form):
    name=forms.CharField(widget=forms.FileInput)
    email=forms.EmailField(widget=forms.CheckboxInput)
    address=forms.CharField(widget=forms.TextInput(attrs={'name':'somecss','id':'my_object'}))
    passwor=forms.CharField(widget=forms.PasswordInput())
    