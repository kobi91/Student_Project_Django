from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns=[
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.home, name='home'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('students_table', views.students_table, name='students_table'),
    path('courses_table', views.courses_table, name='courses_table'),
    path('statistics_table', views.statistics_table, name='statistics_table'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('manager', views.manager, name='manager'),
]
