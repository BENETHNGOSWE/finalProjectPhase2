from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Mtihani
from .forms import ExamForm,MtihaniForm
from FYPAPP.models import QCategory, QuestionChoice, QuestionShortterm, QuestionLongTerm, Course
from FYPAPP.forms import QCategoryForm, QuestionChoiceForm
from django.db import connection
import random
from .pdf import html_to_pdf 
from django.views.generic import View
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from django.template.loader import render_to_string
from weasyprint import HTML


def exam_manage(request):
    context = {'exam_manage': Mtihani.objects.all()}
    # context2 = {'question_choice': QuestionChoice.objects.all()}
    return render(request, "mtihani/exam_manage.html", context)



def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
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

# class select_questions(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'mtihani/generate_exam.html')
    
#     def post(self, request, *args, **kwargs):
#         # Retrieve num_questions, num_shortquestions, and num_longquestions values from POST request
#         num_questions = int(request.POST.get('num_questions'))
#         num_shortquestions = int(request.POST.get('num_shortquestions'))
#         num_longquestions = int(request.POST.get('num_longquestions'))
        
#         # Retrieve questions from database and shuffle them
#         questions = list(QuestionChoice.objects.all())
#         random.shuffle(questions)
        
#         questionshort = list(QuestionShortterm.objects.all())
#         random.shuffle(questionshort)
        
#         questionlong = list(QuestionLongTerm.objects.all())
#         random.shuffle(questionlong)
        
#         # Save only the required number of questions
#         questions = questions[:num_questions]
#         for question in questions:
#             question.save()
        
#         questionshort = questionshort[:num_shortquestions]
#         for question in questionshort:
#             question.save()
        
#         questionlong = questionlong[:num_longquestions]
#         for question in questionlong:
#             question.save()
        
#         # Create a context containing the questions
#         context = {
#             'num_questions': num_questions,
#             'num_shortquestions': num_shortquestions,
#             'num_longquestions': num_longquestions,
#             'questions': questions,
#             'questionshort': questionshort,
#             'questionlong': questionlong,
#         }
        
#         # Render the HTML template with the context
#         html = render_to_string('pdf2.html', {'questions': questions, 'questionshort': questionshort, 'questionlong': questionlong})
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'filename="questions.pdf"'
#         buffer = BytesIO()
#         HTML(string=html).write_pdf(buffer)
#         response.write(buffer.getvalue())

#         # Return the PDF as an HTTP response
#         return response



class select_questions(View):
    def get(self, request, *args, **kwargs):
        form = MtihaniForm()
        return render(request, 'mtihani/generate_exam.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = MtihaniForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            semeter = form.cleaned_data['semeter']
            module = form.cleaned_data['module']
            modulecode = form.cleaned_data['modulecode']
            exam_name = form.cleaned_data['exam_name']
            examtime = form.cleaned_data['examtime']
            examdate = form.cleaned_data['examdate']
            examinationDescription = form.cleaned_data['examinationDescription']
            examinationDescription2 = form.cleaned_data['examinationDescription2']
            examinationDescription3 = form.cleaned_data['examinationDescription3']
            num_questions = form.cleaned_data['num_questions']
            num_shortquestions = form.cleaned_data['num_shortquestions']
            num_longquestions = form.cleaned_data['num_longquestions']

            
        
        # Retrieve questions from database and shuffle them
        questions = list(QuestionChoice.objects.all())
        random.shuffle(questions)
        
        questionshort = list(QuestionShortterm.objects.all())
        random.shuffle(questionshort)
        
        questionlong = list(QuestionLongTerm.objects.all())
        random.shuffle(questionlong)
        
        # Save only the required number of questions
        questions = questions[:num_questions]
        for question in questions:
            question.save()
        
        questionshort = questionshort[:num_shortquestions]
        for question in questionshort:
            question.save()
        
        questionlong = questionlong[:num_longquestions]
        for question in questionlong:
            question.save()
        
        # Create a context containing the questions, semester, and exam_name
        context = {
            'course': course,
            'semeter': semeter,
            'module': module,
            'modulecode' : modulecode,
            'exam_name': exam_name,
            'examdate': examdate,
            'examtime': examtime,
            'examinationDescription':examinationDescription,
            'examinationDescription2':examinationDescription2,
            'examinationDescription3':examinationDescription3,
            'num_questions': num_questions,
            'num_shortquestions': num_shortquestions,
            'num_longquestions': num_longquestions,
            'questions': questions,
            'questionshort': questionshort,
            'questionlong': questionlong,
        }
        
        # Render the HTML template with the context
        html = render_to_string('pdf2.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="questions.pdf"'
        buffer = BytesIO()
        HTML(string=html).write_pdf(buffer)
        response.write(buffer.getvalue())

        # Return the PDF as an HTTP response
        return response
        
        return render(request, 'mtihani/generate_exam.html', {'form': form})
   
        