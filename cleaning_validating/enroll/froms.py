from django import forms
class Student(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField()
    def clean_password(self):
        my_add=self.cleaned_data['password']
        if len(my_add)<10:
            raise forms.ValidationError('please enter your complete chars more than 4')
        return my_add    