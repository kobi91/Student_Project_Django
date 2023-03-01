from django import forms
from Students.models import Student, Course, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'id', 'address', 'phone', 'email', 'course']
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        