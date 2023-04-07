from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from .forms import ExamForm
from FYPAPP.models import QCategory, QuestionChoice, QuestionShortterm, QuestionLongTerm
from FYPAPP.forms import QCategoryForm, QuestionChoiceForm
from django.db import connection
import random
from .pdf import html_to_pdf 
from django.views.generic import View
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa





def GeneratePdf(request):
    # Render the HTML template to a PDF
    template = get_template('mtihani/generate_exam.html')
    html = template.render()
    response = BytesIO()
    pdf = pisa.CreatePDF(html, dest=response)
    
    # Return the PDF as a response
    if pdf.err:
        return HttpResponse('Error generating PDF')
    response.seek(0)
    return HttpResponse(response, content_type='application/pdf')

# def GeneratePdf(request, *args, **kwargs):
#     # getting the template
#     pdf = html_to_pdf('mtihani/generate_exam.html')
   
#     # rendering the template
#     return HttpResponse(pdf, content_type='application/pdf')
# def GeneratePdf(request, *args, **kwargs):
#     question = QuestionChoice.objects.all()
#     context = {
#         'question': question
#     }
#     pdf = html_to_pdf('mtihani/generate_exam.html', context)
#     return HttpResponse(pdf, content_type='application/pdf')




# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
         
#         # getting the template
#         pdf = html_to_pdf('generate_exam.html')
         
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')
# Create your views here

def exam_manage(request):
    context = {'exam_manage': Exam.objects.all()}
    context2 = {'question_choice': QuestionChoice.objects.all()}
    return render(request, "mtihani/exam_manage.html", context)

# def add_exam(request):
#     # chaguamaswali = input("chagua")
#     questionType = QCategory.objects.defer('questionType')
#     # option
#     # QuestionType = QCategory.objects.all()
#     # questionType = QCategory.objects.filter(id=2).only('questionType')

#     if request.method == "POST":
#         form = ExamForm(request.POST) 
#         form2 = QuestionChoiceForm(request.POST) 
#         if form.is_valid():
#             form.save()
#         return redirect('/exam')  

#     else:
#         form = ExamForm()
#         form2 = QuestionChoiceForm()
#         context = {"form":form, "form2":form2, "questionType":questionType}
#         return render(request, "mtihani/add_exam.html", context)


def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()

            num_questions = int(request.POST.get('num_questions'))
            questions = list(QuestionChoice.objects.all())
            random.shuffle(questions)
            questions = questions[:num_questions]
            # questions.save()

            questionshort = list(QuestionShortterm.objects.all())
            random.shuffle(questionshort)
            questionshort = questionshort[:num_questions]
            # questionshort.save()

        
            # questionlong = list(QuestionLongTerm.objects.all())
            # return redirect('/exam')
        return redirect('/exam')  

    else:
            form = ExamForm()
            return render(request, "mtihani/add_exam.html", {"form":form})     








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





def select_questions(request):
    form = ExamForm(request.POST)
    # multiplechoice question algorithms
    if request.method == 'POST':
        num_questions = int(request.POST.get('num_questions'))
        questions = list(QuestionChoice.objects.all())
        random.shuffle(questions)
        questions = questions[:num_questions]


        # short question algorithms
        num_shortquestions = int(request.POST.get('num_shortquestions'))
        questionshort = list(QuestionShortterm.objects.all())
        random.shuffle(questionshort)
        questionshort = questionshort[:num_shortquestions]
        
        # long question algorithms
        num_longquestions = int(request.POST.get('num_longquestions'))
        questionlong = list(QuestionLongTerm.objects.all())
        random.shuffle(questionlong)
        questionlong = questionlong[:num_longquestions]

        context = {
            'questions':questions,
            'questionshort':questionshort,
            'questionlong':questionlong,

        }
        # pass the selected questions to the template
        return render(request, "mtihani/generate_exam.html", context)
    else:
        form = ExamForm()
        return render(request, 'mtihani/add_exam.html', {"form":form})


# def add_exam(request):
#     if request.method == "POST":
#         form = ExamForm(request.POST)
#         if form.is_valid():
#             exam = form.save()
#             num_questions = int(request.POST.get('num_questions'))
#             questions = list(QuestionChoice.objects.all())
#             random.shuffle(questions)
#             questions = questions[:num_questions]
#             questionshort = list(QuestionShortterm.objects.all())
#             random.shuffle(questionshort)
#             questionshort = questionshort[:num_questions]
#             return redirect('/exam')
#             # return render(request, "mtihani/exam_manage.html", {  })
#     else:
       
#         context = {
#             'form':form,
#             'exam': exam,
#             'questions': questions,
#             'questionshort': questionshort
#         }
#     return render(request, "mtihani/add_exam.html", context)
