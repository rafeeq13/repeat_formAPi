from django.shortcuts import render
from .froms import Student
# Create your views here.
def sudden(request):
    return render(request,'enroll/success.html')
def details(request):
    if request.method=='POST':
        st=Student(request.POST)
        if st.is_valid():
            password=st.cleaned_data['password']
            rpassword=st.cleaned_data['rpassword']
            print(password,rpassword)

            
    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})