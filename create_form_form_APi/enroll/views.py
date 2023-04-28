from django.shortcuts import render

# Create your views here.
from .froms import Student
def detail(request):
    st=Student()
    return render(request,'enroll/student.html',{'form':st})
