from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from authentication.models import Profile,Teacher,Student
# Create your models here.



class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='course_teacher')
    course_name= models.CharField(max_length=150)
    chapter = models.ForeignKey('Chapter',blank=True,null=True,on_delete=models.CASCADE,related_name='course_chapter')
    course_description = models.TextField()
    price = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    total_lessons=models.IntegerField(null=True, blank = True)
    course_image = models.ImageField(upload_to='courses_images')

    def __str__(self) -> str:
        return self.course_name
    

class Chapter(models.Model):
    course = models.ForeignKey(Course ,on_delete=models.CASCADE,related_name='course_chapter',blank=True,null=True)
    name = models.CharField(max_length=150)
    num_of_lessons = models.IntegerField(default=0)

    

    
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter ,on_delete=models.CASCADE,related_name='chapter_lesson',blank=True,null=True)
    lesson_name = models.CharField(max_length=200)
    lesson_description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    lesson_video_file = models.FileField(upload_to='videos/',
                                  validators=[FileExtensionValidator(
                                      ['mp4', 'mkv', 'wmv', '3gp', 'f4v', 'avi', 'mp3']
                                      )],blank=True,null=True)
    lesson_text_file = models.TextField(blank=True,null=True)
    quiz = models.TextField(blank=True,null=True)


 
