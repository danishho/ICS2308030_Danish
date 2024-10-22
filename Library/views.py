from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Library.models import Student, Book, Borrowing, Course, Mentor


# Create your views here.

def index(request):
    context = {
        'greeting': 0
    }
    return render(request, 'index.html',context)

def view(request):
    context = {
        'name':'khalled ****'
    }

    return render(request, 'view.html',context)

def database(request):
    student = Student.objects.all().values()
    book = Book.objects.all().values()
    borrowing = Borrowing.objects.select_related('book_id', 'student_id').all()

    context = {
        'student': student,
        'book': book,
        'borrowing': borrowing
    }
    return render(request, 'database.html',context )



def course(request):
    course = Course.objects.all().values()
    if request.method == 'POST':
        code = request.POST['code']
        description = request.POST['desc']
        data = Course(code=code, description=description)
        data.save()
        dict = {
            'message':'berjaya',
            'course':course
        }
    else:
        dict = {
            'message':'tidak',
            'course': course
        }
    return render(request, 'course.html',dict)


def mentor(request):
    mentor = Mentor.objects.all().values()
    dict = {
        'mentor': mentor
    }
    if request.method == 'POST':
        mentorid= request.POST['mentor_id']
        menname = request.POST['mentor_name']
        menroom = request.POST['mentor_room']
        data = Mentor(menid=mentorid,menname=menname,menroomno = menroom)
        data.save()

    return render(request,'newmentor.html',dict)

def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
        'course':data
    }
    return render(request, 'update_course.html', dict)

def save_update_course(request,code):
    description = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = description
    data.save()
    return HttpResponseRedirect(reverse('course'))

def update_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    dict ={
        'mentor':data
    }
    return render(request, 'update_mentor.html', dict)

def save_update_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    name = request.POST['mentor_name']
    room = request.POST['mentor_room']
    data.menname = name
    data.menroomno = room
    data.save()
    return HttpResponseRedirect(reverse('mentor'))


def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

def delete_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    data.delete()
    return HttpResponseRedirect(reverse('mentor'))


def search(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')
        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        context = {
            'data': data
        }
        return render(request, 'search_course.html', context)
    return render(request, 'search_course.html')



