from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Account(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    id = models.IntegerField(default=0, primary_key=True)
    is_active = models.BooleanField(default=True)
    authorization = models.CharField(max_length=256)
    date_joined = models.DateTimeField(default=timezone.now)
    
    def user_login(self, authorization):   
        if authorization == "master":
            return "manager"
        elif authorization == "teacher":
            return "teacher"    
        elif authorization == "student":
            return "students"
        else: 
            return None
    
    def __str__(self):
        return self.username, self.email
                   
    def __repr__(self):
        return self.__str__()

class Student(models.Model):
    name = models.CharField(max_length=256, unique=True)
    age = models.IntegerField(default=0)
    id = models.IntegerField(default=0, primary_key=True)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    course = models.CharField(max_length=256)
    grade = models.IntegerField(default=0)
    missing = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name, self.age, self.id, self.address, self.phone, self.email, self.course, self.grade, self.missing
                   
    def __repr__(self):
        return self.__str__()

class Course(models.Model):
    name = models.CharField(max_length=256, unique=True)
    students_number = models.IntegerField(default=0)
    average_grade = models.IntegerField(default=0)
    passed_percentage = models.IntegerField(default=0)
    description = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name, self.students_number, self.average_grade, self.passed_percentage, self.description
                   
    def __repr__(self):
        return self.__str__()

    
class Registeration(models.Model):
    code = models.CharField(max_length=256, unique=True)
    authorization = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.code, self.authorization
                   
    def __repr__(self):
        return self.__str__()   
    
class Teacher(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    
    def __str__(self):
        return self.name, self.email
                   
    def __repr__(self):
        return self.__str__()
 
    
@receiver(post_migrate)    
def default(sender, **kwargs): 
    try:
        if sender.name == 'Students': 
            Registeration.objects.get_or_create(code='1111', authorization='student')
            Registeration.objects.get_or_create(code='2222', authorization='teacher')
            Account.objects.create_user(id=1, username='manager', password='1234', email='manager@manager.com', authorization='master')  
    except:
        None