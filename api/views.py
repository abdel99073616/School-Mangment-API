from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from A.models import(
    Parent_A ,
    Activites_A ,
    Course_A ,
    Classroom_A ,
    Student_A ,
    Teacher_A
)

from .serializers import(
    ParentSerializer ,
    ActivitesSerializer ,
    ClassroomSerializer ,
    CourseSerializer ,
    StudentSerializer ,
    TeacherSerializer
)

class ParentListAPIVeiw(ListAPIView):
    queryset = Parent_A.objects.all()
    serializer_class = ParentSerializer
class ParentRetrieveAPIView(RetrieveAPIView):
    queryset = Parent_A.objects.all()
    serializer_class = ParentSerializer

class ActivitesListAPIVeiw(ListAPIView):
    queryset = Activites_A.objects.all()
    serializer_class = ActivitesSerializer
class ActivitesRetrieveAPIView(RetrieveAPIView):
    queryset = Activites_A.objects.all()
    serializer_class = ActivitesSerializer

class ClassroomListAPIVeiw(ListAPIView):
    queryset = Classroom_A.objects.all()
    serializer_class = ClassroomSerializer
class ClassroomRetrieveAPIView(RetrieveAPIView):
    queryset = Classroom_A.objects.all()
    serializer_class = ClassroomSerializer

class CoursesListAPIVeiw(ListAPIView):
    queryset = Course_A.objects.all()
    serializer_class = CourseSerializer
class CoursesRetrieveAPIView(RetrieveAPIView):
    queryset = Course_A.objects.all()
    serializer_class = CourseSerializer

class StudentListAPIVeiw(ListAPIView):
    queryset = Student_A.objects.all()
    serializer_class = StudentSerializer
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student_A.objects.all()
    serializer_class = StudentSerializer

class TeacherListAPIVeiw(ListAPIView):
    queryset = Teacher_A.objects.all()
    serializer_class = TeacherSerializer
class TeacherRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher_A.objects.all()
    serializer_class = TeacherSerializer
