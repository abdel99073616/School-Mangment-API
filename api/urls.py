from django.contrib import admin
from django.urls import path , include
from .views import(
    ParentListAPIVeiw,
    ParentRetrieveAPIView ,
    
)



urlpatterns = [
    path('Parent/' , ParentListAPIVeiw.as_view() ) ,
    path('Parent/<pk>' , ParentRetrieveAPIView.as_view() )
]
