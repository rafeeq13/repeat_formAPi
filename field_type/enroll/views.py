from django.shortcuts import render
from .froms import Student
from django.http import HttpResponseRedirect
# Create your views here.
def sudden(request):
    return render(request,'enroll/success.html')
def details(request):
    if request.method=='POST':
        st=Student(request.POST)
        if st.is_valid():
            print(st)
            name=st.cleaned_data ['name']
            password=st.cleaned_data['password']
            print(type(password))

            
    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})