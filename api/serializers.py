from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
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



class ParentSerializer(ModelSerializer):
    class Meta :
        model = Parent_A
        fields = '__all__'