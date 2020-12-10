from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from A.models import(
    Parent_A ,
    Activites_A ,
    Activites_student_teacher_A ,
    Course_A ,
    Classroom_A ,
    Student_A ,
    Student_Course_A ,
    Sudent_Teacher_A ,
    Teacher_A
)

from .serializers import(
    ParentSerializer ,
)

class ParentListAPIVeiw(ListAPIView):
    queryset = Parent_A.objects.all()
    serializer_class = ParentSerializer

class ParentRetrieveAPIView(RetrieveAPIView):
    queryset = Parent_A.objects.all()
    serializer_class = ParentSerializer
