
from django.urls import path
from . import views
appname = 'dashboard'
urlpatterns = [
    path('', views.user_view,name='users_view'),
    path('users/details/<int:id>', views.user_detail,name='details'),
    path('users/update/<int:id>', views.user_update,name='update'),   
    path('users/create_user/', views.create_user,name='create_user'), 
    # course management urls
        # Course
    path('courses/view/', views.course_view,name='course_managment_views'),
    path('courses/create/', views.course_crate,name='course_managment_create'),
    path('courses/details/<int:id>', views.course_details,name='course_managment_details'),
    path('courses/edit/<int:id>', views.course_edit,name='course_managment_edit'),
    path('courses/course_delete/<int:id>', views.course_delete,name='course_managment_delete'),
        # Chapter
    
    path('courses/chapter_create/<int:id>', views.chapter_create,name='chapter_create'),
    path('courses/chapter_update/<int:id>', views.chapter_update,name='chapter_update'),
    path('courses/chapter_delete/<int:id>', views.chapter_delete,name='chapter_delete'),
        # Lesson
    path('courses/lesson_view/<int:id>', views.lesson_view,name='lesson_view'),
    path('courses/lesson_create/<int:id>', views.lesson_create,name='lesson_create'),
    path('courses/lesson_edit/<int:id>', views.lesson_edit,name='lesson_edit'),
    path('courses/lesson_delete/<int:id>', views.lesson_delete,name='lesson_delete'),
]
