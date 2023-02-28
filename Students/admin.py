from django.contrib import admin
from .models import Student, Course, Registeration, Teacher

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Registeration)
admin.site.register(Teacher)
