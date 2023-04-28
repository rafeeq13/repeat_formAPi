from django.shortcuts import render
from .forms import Student
# Create your views here.
def details(request):
    st=Student(auto_id=True,label_suffix='- ',initial={'name':'rafeeq','email':'rafeeq@gmail.com'})
    return render(request,'enroll/student.html',{'form':st})