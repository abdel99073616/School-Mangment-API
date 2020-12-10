from django.contrib import admin
from django.urls import path , include
from .views import(
    ParentListAPIVeiw,
    ParenCreateAPIVeiw ,
    ParentRetrieveAPIView ,
    ParentDestroyAPIView ,
    ParentUpdateAPIView ,
    ActivitesListAPIVeiw ,
    ActivitesRetrieveAPIView ,
    ClassroomListAPIVeiw ,
    ClassroomRetrieveAPIView ,
    CoursesListAPIVeiw ,
    CoursesRetrieveAPIView ,
    StudentListAPIVeiw ,
    StudentRetrieveAPIView ,
    TeacherListAPIVeiw ,
    TeacherRetrieveAPIView
)

urlpatterns = [
    path('Parent/' , ParentListAPIVeiw.as_view() ) ,
    path('Parent/create' , ParenCreateAPIVeiw.as_view() ) ,
    path('Parent/<pk>' , ParentRetrieveAPIView.as_view() ) ,
    path('Parent/<pk>/edit' , ParentUpdateAPIView.as_view() ) ,
    path('Parent/<pk>/delete' , ParentDestroyAPIView.as_view() ) ,
    
    path('Acticites/' , ActivitesListAPIVeiw.as_view() ) ,
    path('Acticites/<pk>' , ActivitesRetrieveAPIView.as_view() ) ,
    
    path('Classroom/' , ClassroomListAPIVeiw.as_view() ) ,
    path('Classroom/<pk>' , ClassroomRetrieveAPIView.as_view() ) ,
    
    path('Courses/' , CoursesListAPIVeiw.as_view() ) ,
    path('Courses/<pk>' , CoursesRetrieveAPIView.as_view() ) ,
    
    path('Courses/' , CoursesListAPIVeiw.as_view() ) ,
    path('Courses/<pk>' , CoursesRetrieveAPIView.as_view() ) ,
    
    path('Student/' , StudentListAPIVeiw.as_view() ) ,
    path('Student/<pk>' , StudentRetrieveAPIView.as_view() ) ,
    
    path('Teacher/' , TeacherListAPIVeiw.as_view() ) ,
    path('Teacher/<pk>' , TeacherRetrieveAPIView.as_view() ) ,
    
]
