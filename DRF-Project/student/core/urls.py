from django.contrib import admin
from django.urls import path, include
from .views import home, StudentItemViews # listStudents, createStudents, detailStudents, 

urlpatterns = [
    path('home', home, name='home'),
    path('Students/', StudentItemViews.as_view(), name='toto_student'),
    path('Students/<int:id>', StudentItemViews.as_view(), name='detail_student'),
    path('Students/', StudentItemViews.as_view(), name='create_student'),
    path('Students/<int:id>', StudentItemViews.as_view(), name='update_student'),
]
