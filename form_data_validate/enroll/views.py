from django.shortcuts import render
from .froms import Student
# Create your views here.
def details(request):
    if request.method=='POST':
        st=Student(request.POST)
        if st.is_valid():
            print(st)
            print(st.cleaned_data ['name'])
    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})