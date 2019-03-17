from django.shortcuts import render
from . models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render('student_list.html', {'students': students})

def submit_attendance(request):
    if request.method=="POST":
        