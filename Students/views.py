from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Course, Student, Registeration, Account
from .forms import StudentForm, CourseForm, TeacherForm
from django.db import connection


#------------------ H O M E  W E B ---------------------# 

def home(request):
    return render(request, "home.html")

def students_table(request):
    return render(request, "students_table.html")

def courses_table(request):
    return render(request, "courses_table.html")     

def statistics_table(request): 
    return render(request, "statistics_table.html")     

def about(request):  
    return render(request, "about.html")


#--------------- L O G I N / L O G O U T ---------------#

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            authorization = Account.objects.values_list('authorization').filter(username=username)
            route = Account.user_login(request, authorization[0][0])
            return redirect(route)   
        else:
            messages.error(request, "Invalid username or password. Please try again!")
    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


#-------------- R E G I S T E R A T I O N --------------#

def register(request):
    if request.method == 'POST':    
        username = request.POST["username"]
        password = request.POST["password"]
        id_ = request.POST["id_"]
        email = request.POST["email"]
        reg_code = request.POST["reg_code"]
        try:
            if reg_code and username and password and email:
                authorization = Registeration.objects.all().values_list().filter(code=reg_code)
                if not authorization:
                    messages.error(request, "Registration code incorrect. Please try again!")
                else:
                    Account.objects.create_user(id=id_, username=username, password=password, email=email, authorization=authorization[0][2])
                    return render(request, "successfully.html", {'username': username})
            else:
                messages.error(request, "Please make sure all fields are filled in correctly.")
        except:
            messages.error(request, "Username or Email already exists. Please try again!")
    return render(request, "register.html")


#-------------- M A N A G E R  P A N E L ---------------#

@login_required
def manager(request):
    return render(request, "manager.html")

@login_required
def manage_students(request):  
    students = Student.objects.all().values_list() 
    return render(request, "manage_students.html", {'students': students, "courses": ['Python','Java']})     
 
@login_required 
def add_student(request):
    if request.method == 'POST':
        try:
            student_data = {k:v.title() for k,v in request.POST.items()}       
            students = Student(**student_data)
            students.save()
        except:
            messages.error(request, "Please make sure all fields are filled in correctly.")      
    return redirect('manage_students')

@login_required 
def delete_student(request):
    id = request.POST["student"]
    student = Student.objects.get(pk = id)
    student.delete()
    return HttpResponse('deleted')


#-------------- T E A C H E R  P A N E L ---------------#

@login_required
def teacher(request):
    return render(request, "teacher.html")




def update(request, id):
   emp = Student.objects.get(pk = id)
   emp.name = request.POST.get('name')
   emp.save()
   return HttpResponse('updated')

def delete(id):
   emp = Student.objects.get(pk = id)
   emp.delete()
   return HttpResponse('deleted')


