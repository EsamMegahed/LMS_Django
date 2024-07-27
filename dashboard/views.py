from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserView
from django.contrib.auth.models import User
from .forms import UserForms,UserCreate,CreateChapter,CreateCourse,CreateLesson
from django.core.paginator import Paginator
from django.contrib import messages
from .filters import UsersFilter

from courses.models import Course,Chapter,Lesson
# Create your views here.

# User Mangement functions

def user_view(request):
    users = User.objects.all()
    user_filter = UsersFilter(request.GET,queryset=users)
    users = user_filter.qs
    
    paginator = Paginator(users,2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {'users':page_obj,
               'user_filter':user_filter}
    return render(request, "user_view.html", context)

def user_detail(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Account Deleted successfully')
        return redirect(reverse("users_view"))
    context= {
        'user':user,
        
    }
    return render(request, "user_details.html", context)


def user_update(request,id):
    user = User.objects.get(id= id)
    
    if request.method == 'POST':
        form = UserForms(request.POST,instance=user)
        if form.is_valid():
            form.save() 
            return redirect(reverse("details",args=[user.id]))
    else:
        form = UserForms(instance=user)
    context = {
        'form' : form
    }
    return render(request, "user_update.html", context)


def create_user(request):
    if request.method == "POST":  
        form = UserCreate(request.POST)  
        if form.is_valid():  
            form.save()  
            
            messages.success(request, 'Account created successfully')

            return redirect(reverse("users_view"))
  
    else:  
        form = UserCreate()  
    context = {
        'form':form
    }

    return render(request, "user_add.html", context)




# Courses Mangement functions - - - - - - -

    # ---------------------------- Course ----------------------------

def course_view(request):
    courses = Course.objects.all()

    context = {'courses':courses}
    return render(request,"courses_templates/course_view.html", context)

def course_crate(request):
    if request.method == 'POST':
        form =CreateCourse(request.POST,request.FILES)
        if form.is_valid():
            teacher = form.cleaned_data['teacher']
            course_name = form.cleaned_data['course_name']
            course_description = form.cleaned_data['course_description']
            course_image = form.cleaned_data['course_image']
            price = form.cleaned_data['price']
            course_create = Course.objects.create(
                teacher=teacher,
                course_name=course_name,
                course_description=course_description,
                price=price,
                course_image=course_image
            )
            
            course = Course.objects.get(id=course_create.id)
            return redirect(reverse('course_managment_details',args=[course.id]))
    else:
        form =CreateCourse()
    context = {'form':form}
    return render(request,"courses_templates/course_create.html", context)

def course_edit(request,id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form =CreateCourse(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
            return redirect(reverse('course_managment_details',args=[course.id]))
    else:
        form =CreateCourse(instance=course)

    context = {'form':form}

    return render(request,"courses_templates/course_edit.html", context)



def course_details(request,id):
    course = Course.objects.get(id=id)
    chapters = course.course_chapter.all()

    total_lessons = 0
    total_chapters = 0
    
    for chapter in chapters:
        total_chapters += 1
        for lesson in chapter.chapter_lesson.all():
            total_lessons += 1
        
    context = {'chapter':chapters,
               'course':course,
               'total_lessons':total_lessons,
               'total_chapters':total_chapters,
    }
    return render(request,"courses_templates/course_mangement_details.html", context)
    
def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return HttpResponseRedirect(reverse('course_managment_views'))



    # ---------------------------- Chapter ----------------------------
def chapter_create(request,id):
    course = Course.objects.get(id=id)
    
    if request.method == "POST":  
        form = CreateChapter(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           chapter =  Chapter.objects.create(course=course,name=name)
           chapter.save()
           return redirect(reverse('course_managment_details',args=[course.id]))
    else:
        form = CreateChapter() 

        context = {
            'form':form
        }
    return render(request,"courses_templates/course_management_chapter_create.html", context)

def chapter_update(request,id):
    chapter = Chapter.objects.get(id=id)
    if request.method == 'POST':
        form =CreateChapter(request.POST,instance=chapter)
        if form.is_valid():
            form.save()

            return redirect(reverse('course_managment_details',args=[chapter.course.id]))
    else :
        form = CreateChapter(instance=chapter)

    context = {
        'form':form
    }
    return render(request,"courses_templates/course_management_chapter_update.html", context)


def chapter_delete(request, id): 
    chapter = Chapter.objects.get(id=id)
    chapter.delete()
    
    return HttpResponseRedirect(reverse('course_managment_details',args=[chapter.course.id]))

    # ---------------------------- Lesson ----------------------------

def lesson_view(request,id):
    lesson = Lesson.objects.get(id=id)
    
    context = {
        'lesson':lesson
    }
    return render(request,"courses_templates/course_management_lesson_view.html", context)

def lesson_create(request,id):
    chapter = Chapter.objects.get(id=id)
    if request.method == "POST":
        form = CreateLesson(request.POST,request.FILES)
        if form.is_valid():
            lesson_name = form.cleaned_data['lesson_name']
            lesson_description = form.cleaned_data['lesson_description']
            lesson_video_file = form.cleaned_data['lesson_video_file']
            lesson_text_file = form.cleaned_data['lesson_text_file']
            quiz = form.cleaned_data['quiz']
            lesson_create = Lesson.objects.create(
                chapter=chapter,
                lesson_name=lesson_name,
                lesson_description=lesson_description,
                lesson_video_file=lesson_video_file,
                lesson_text_file=lesson_text_file,
                quiz=quiz,
            )
            return redirect(reverse('course_managment_details',args=[chapter.course.id]))
    else:
        form = CreateLesson()

    context = {
            'form':form
        }
    return render(request,"courses_templates/course_management_lesson_create.html", context)

def lesson_edit(request,id):
    lesson = Lesson.objects.get(id=id)
    if request.method == "POST":
        form = CreateLesson(request.POST,request.FILES,instance=lesson)
        if form.is_valid():
            form.save()
            return redirect(reverse('lesson_view',args=[lesson.id]))
    else:

        form = CreateLesson(instance=lesson)
    context = {
        'form':form
    }
    return render(request,"courses_templates/course_management_lesson_update.html", context)

def lesson_delete(request,id):
    lesson = Lesson.objects.get(id=id)
    lesson.delete()
    return HttpResponseRedirect(reverse('course_managment_details',args=[lesson.chapter.course.id]))