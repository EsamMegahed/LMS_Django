from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    status_choices = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher')
    )
    status = models.CharField(max_length=200,
                               choices=status_choices,
                                 blank=True,
                                   null=True,
                                     default='Student')
    
    image_profile = models.ImageField(null=True, blank=True, default='blank.png', upload_to='user_profile/')
    github = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instgram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

class Teacher(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,related_name='teacher')
    qualification = models.CharField(max_length=2000, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    def __str__(self) -> str:
        return str(self.profile)

class Student(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,related_name='student')
    date_of_birth = models.DateField(blank=True, null=True)
    def __str__(self) -> str:
        return str(f'Student : {self.profile}')