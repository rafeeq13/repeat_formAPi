from django.shortcuts import render
from .forms import Student
# Create your views here.
def details(request):
    st=Student()
    st.order_fields(field_order=['email','name'])
    return render(request,'enroll/student.html',{'form':st})