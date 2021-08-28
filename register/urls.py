
from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
    path('add-student', RegisterStudent.as_view()),
    path('get-students', GetStudent.as_view()),

    path('add-subject', AddSubject.as_view()),
    path('get-subjects', GetSubject.as_view()),

    path('register-subject', RegisterSubject.as_view()),

    path('unregister-subject', UnregisterSubject.as_view()),

]
