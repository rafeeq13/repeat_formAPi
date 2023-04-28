from django import forms
class Student(forms.Form):
    name=forms.CharField(initial='sonam')
    email=forms.EmailField(initial='rafeeq@gmail.com')