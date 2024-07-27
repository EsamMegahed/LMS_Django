from django.shortcuts import render
from django.views.generic import ListView
from .models import Course,Chapter,Lesson

# Create your views here.


def test(request):
    context = {}
    return render(request,'course_list.html',context)


class CoursesList(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course_list.html'


def course_details(request,id):
    course = Course.objects.get(id=id)
    chapter = course.course_chapter.all()

    context = {'chapter':chapter,
               'course':course}
    return render(request,'course_details.html',context)

def course_lesson(request,id):
    lesson = Lesson.objects.get(id=id)
    context = {'lesson':lesson}
    return render(request,'lesson.html',context)
