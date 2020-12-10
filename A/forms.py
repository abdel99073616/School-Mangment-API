from django import forms
from .models import  Student_A ,Student_Course_A , Activites_A , Activites_student_teacher_A , Classroom_A ,Course_A , Parent_A , Sudent_Teacher_A , Teacher_A
from django.forms import ModelChoiceField

#################################################################################
# Teacher Form

class TeacherForm_A(forms.ModelForm):
    class Meta:
        model = Teacher_A
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'Email' ,
            'last_login',
        ]
   
class TeacherRowForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()

#################################################################################

# Parent Form

class ParentForm_A(forms.ModelForm):
    class Meta:
        model = Parent_A
        fields =[
            'Father_name' ,
            'Mother_name' ,
            'address' ,
            'Phone' ,
            'password' ,
            'last_login',
        ]
   
class ParentRowForm_A(forms.Form):
    Father_name = forms.CharField()
    Mother_name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    password = forms.CharField()
    last_login = forms.DateTimeField()

###############################################################################
# Course Form

class CourseForm_A(forms.ModelForm):
    class Meta:
        model = Course_A
        fields =[
            'name' 
        ]
   
class CourseRowForm_A(forms.Form):
    name = forms.CharField()

#################################################################################

# Student Form

class ClassroomForm_A(forms.ModelForm):
    class Meta:
        model = Classroom_A
        fields =[
            'Student_Level' ,
            'section' ,
        ]

class ClassroomRowForm_A(forms.Form):
    Student_Level = forms.CharField()
    section = forms.CharField()

#################################################################################

# Student Form

class ActivitiesForm_A(forms.ModelForm):
    class Meta:
        model = Activites_A
        fields =[
            'act_name' ,
            'Date' ,
            'type_of_activite' ,
        ]
   
class ActivitiesRowForm_A(forms.Form):
    act_name = forms.CharField()
    Date = forms.CharField()
    type_of_activite = forms.CharField()


#################################################################################


# Student Form

class StudentForm_A(forms.ModelForm):
    class Meta:
        model = Student_A
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'parent_ID' ,
            'Class_ID' ,
            'level_ID_A' ,
        ]
   
class StudentRowForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    parent_ID = forms.ChoiceField()
    Class_ID = forms.ChoiceField()
    level_ID_A = forms.ChoiceField()



