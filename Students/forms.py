from django import forms
from django.contrib.auth.forms import UserCreationForm
from Students.models import Student, Course, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        