from django import forms
class Student(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField()
    def clean(self):
        cleaned_data=super().clean()
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        if len(name)<4:
            raise forms.ValidationError('ente your name more than 4 chars')
        
        if len(email)<10:
            raise forms.ValidationError('please enter your complete eamil  chars more than 10')
          