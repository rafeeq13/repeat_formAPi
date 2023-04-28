from django.shortcuts import render
from .froms import Student
# Create your views here.
def details(request):
    st=Student()
    return render(request,'enroll/student.html',{'form':st})