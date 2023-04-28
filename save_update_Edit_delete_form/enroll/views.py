from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.
def sudden(request):
    return render(request,'enroll/success.html')
def details(request):
    if request.method=='POST':
        st=Student(request.POST)
        if st.is_valid():
            nm=st.cleaned_data['name']
            em=st.cleaned_data['email']
            ad=st.cleaned_data['address']
            reg=User(id=1,name=nm,email=em,address=ad)
            reg.save()
    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})