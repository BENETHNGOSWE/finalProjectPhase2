from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from .forms import ExamForm
from FYPAPP.models import QCategory, QuestionChoice
from FYPAPP.forms import QCategoryForm, QuestionChoiceForm
from django.db import connection
# Create your views here

# def exam(request):
#     categories = Category.objects.all()
#     questions = []
#     for category in categories:
#         category_questions = Question.objects.filter(category=category).order_by('?')[:2]  # select 5 random questions from each category
#         questions.extend(list(category_questions))
#     random.shuffle(questions) 
    
#      # shuffle the list of questions
#     return render(request, 'generate_exam.html', {'questions': questions})  

def exam_manage(request):
    context = {'exam_manage': Exam.objects.all()}
    context = {'question_choice': QuestionChoice.objects.all()}
    return render(request, "mtihani/exam_manage.html", context)

def add_exam(request):
    # chaguamaswali = input("chagua")
    questionType = QCategory.objects.defer('questionType')
    # option
    # QuestionType = QCategory.objects.all()
    # questionType = QCategory.objects.filter(id=2).only('questionType')

    if request.method == "POST":
        form = ExamForm(request.POST) 
        form2 = QuestionChoiceForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('/exam')  

    else:
        form = ExamForm()
        form2 = QuestionChoiceForm()
        context = {"form":form, "form2":form2, "questionType":questionType}
        return render(request, "mtihani/add_exam.html", context)

    

def update_exam(request, pk):
    mtihani = Exam.objects.get(id=pk)
    form = ExamForm(instance=mtihani)

    if request.method == "POST":
        form = ExamForm(request.POST, instance=mtihani)  
        if form.is_valid():
            form.save()  
            return redirect('/exam')  

    context = {"form":form}
    return render(request, 'mtihani/add_exam.html', context)                  

    

def generate_exam(request):
    # Get the number of questions per category from the request
    num_categories = request.POST.get('num_categories')
    num_questions_per_category = request.POST.get('num_questions_per_category')

    # Get a list of categories
    categories = QCategory.objects.all()

    # Create an empty list to store the selected questions
    questions = []

    # Select the specified number of questions randomly from each category
    for category in categories:
        category_questions = Question.objects.filter(category=category)
        random_questions = random.sample(list(category_questions), num_questions_per_category)
        questions.extend(random_questions)

    # Shuffle the questions randomly
    random.shuffle(questions)

    # Render the exam template with the selected questions
    context = {'questions': questions}
    return render(request, 'mtihani/add_exam.html', context)