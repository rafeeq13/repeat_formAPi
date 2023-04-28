from django.shortcuts import render
from .forms import Student
# Create your views here.
def sudden(request):
    return render(request,'enroll/success.html')
def details(request):
    if request.method=='POST':
        st=Student(request.POST)
        if st.is_valid():
            return render(request,'enroll/student.html',{'form':st})


    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})