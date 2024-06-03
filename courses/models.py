from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from authentication.models import Profile,Teacher,Student
# Create your models here.



class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='course_teacher')
    course_name= models.CharField(max_length=150)
    chapter = models.ForeignKey('Chapter',on_delete=models.CASCADE,related_name='course_chapter')
    course_description = models.TextField()
    price = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    total_lessons=models.IntegerField(null=True, blank = True)

class Chapter(models.Model):
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE,related_name='chapter_lesson')
    name = models.CharField(max_length=150)
    num_of_lessons = models.IntegerField(default=0)

class Lesson(models.Model):
    student = models.ManyToManyField(Student,related_name='student_lesson')
    video = models.ForeignKey('LessonVideo',on_delete=models.CASCADE,related_name='lesson_video',blank=True,null=True)
    text = models.ForeignKey('LessonText',on_delete=models.CASCADE,related_name='lesson_text',blank=True,null=True)
    quiz = models.ForeignKey('LessonQuiz',on_delete=models.CASCADE,related_name='lesson_quiz',blank=True,null=True)


class LessonVideo(models.Model):
    name=models.CharField(max_length=150)
    video_description = models.TextField()
    video_file = models.FileField(upload_to='videos/',
                                  validators=[FileExtensionValidator(
                                      ['mp4', 'mkv', 'wmv', '3gp', 'f4v', 'avi', 'mp3']
                                      )])
    created_at=models.DateTimeField(auto_now_add=True)



class LessonText(models.Model):
    name=models.CharField(max_length=150)
    lesson_text_description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class LessonQuiz(models.Model):
    
    name=models.CharField(max_length=150)
    quiz = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

