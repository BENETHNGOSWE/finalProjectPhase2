from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Course, Masomo, Question,QuestionChoice
from .forms import QuestionForm, CourseForm, MasomoForm, QuestionChoiceForm
from django.db import connection


# Create your views here.


# def home(request):
#     return render(request, 'FYPAPP/home.html')
#     # return render(request,'teacher/teacher_dashboard.html'

# def dashboard(request):
#     return render(request, 'FYPAPP/dashboard.html')


def course_manage(request):
    context = {'course':  Course.objects.all()}
    return render(request, 'FYPAPP/course_manage.html', context)


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/coursedata')   

    else:
        form = CourseForm()
        return render(request, 'FYPAPP/add_course.html', {"form":form})    
         
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/coursedata')

    context = {"form":form}
    return render(request, 'FYPAPP/add_course.html', context)

def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('/coursedata')
# *******************************************************************

def module_manage(request):
    context = {'module_manage': Masomo.objects.all()}
    return render(request, 'FYPAPP/module_manage.html', context)


def add_module(request):
    if request.method == "POST":
        form = MasomoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/moduledata')

    else:
         form = MasomoForm()
         return render(request, 'FYPAPP/add_module.html', {"form":form})           



def update_module(request, pk):
    masomo = Masomo.objects.get(id=pk)
    form = MasomoForm(instance=masomo)

    if request.method == "POST":
        form = MasomoForm(request.POST, instance=masomo)
        if form.is_valid():
            form.save()
            return redirect('/moduledata')

    context = {"form":form}
    return render(request, 'FYPAPP/add_module.html', context)  

# ********************************************************************************* 

# ****************************************************************************





def question_manage(request):
    context = {'question_manage': Question.objects.all()}
    return render(request, "FYPAPP/question_manage.html", context)

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/data')  

    else:
            form = QuestionForm()
            return render(request, "FYPAPP/add_question.html", {"form":form})         


def update_question(request, pk):
    question = Question.objects.get(id=pk)
    form = QuestionForm(instance=question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("/data")

    context = {"form": form }
    return render(request, 'FYPAPP/add_question.html', context)
        

        
def delete_question(request, pk):
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        question.delete()
    return redirect("/data")


    context = {"question":question}
    return render(request, 'FYPAPP/question_manage.html', context)
#   ****************************************************************
def question_choice_manage(request):
    context = {'question_choice': QuestionChoice.objects.all()}
    return render(request, "FYPAPP/question_choice_manage.html", context)


def add_question_choice(request):
    if request.method == "POST":
        form = QuestionChoiceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/choice')
    else:
        form = QuestionChoiceForm()
        return render(request, "FYPAPP/add_question_choice.html", {'form':form})        

def update_question_choice(request, pk):
    question = QuestionChoice.objects.get(id=pk)
    form = QuestionChoiceForm(instance=question)

    if request.method == "POST":
        form = QuestionChoiceForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return redirect('/choice')

    context = {'form':form}
    return render(request, 'FYPAPP/add_question_choice.html', context)

def display(request):
    category = QuestionChoice.objects.filter(category_id=1).only('question')
    print(category)
    print(connection.queries)
    return render(request, "FYPAPP/add_question_choice.html", {'category':category})        



class home(TemplateView):
    template_name = 'FYPAPP/home.html'


class dashboard(TemplateView):
    template_name = 'FYPAPP/dashboard.html'
  






