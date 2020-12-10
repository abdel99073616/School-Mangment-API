from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from A.models import(
    Parent_A ,
    Activites_A ,
    Course_A ,
    Classroom_A ,
    Student_A ,
    Teacher_A
)



class ParentSerializer(ModelSerializer):
    class Meta :
        model = Parent_A
        fields = '__all__'



class ActivitesSerializer(ModelSerializer):
    class Meta :
        model = Activites_A
        fields = '__all__'



class CourseSerializer(ModelSerializer):
    class Meta :
        model = Classroom_A
        fields = '__all__'



class ClassroomSerializer(ModelSerializer):
    class Meta :
        model = Student_A
        fields = '__all__'



class StudentSerializer(ModelSerializer):
    class Meta :
        model = Teacher_A
        fields = '__all__'



class TeacherSerializer(ModelSerializer):
    class Meta :
        model = Course_A
        fields = '__all__'
