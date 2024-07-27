from django.urls import path,include
from . import views
urlpatterns = [

    path('a', views.test),
    path('', views.CoursesList.as_view(),name='site_view_courses'),
    path('course_details/<int:id>', views.course_details,name='site_courses_details'),
    path('course_lesson/<int:id>', views.course_lesson,name='site_course_lesson'),
    
]