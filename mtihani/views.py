from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, ExamQuestion
from .forms import ExamForm, ExamQuestionForm
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
from django.views.generic import ListView
from django.template.loader import render_to_string
from weasyprint import HTML





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

class ExamListView(ListView):
    model = Exam
    template_name = 'main.html'


def exam_render_pdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    exam = get_object_or_404(QuestionChoice, pk=pk)

    template_path = 'pdf2.html'
    context = {'exam': exam}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def exam_manage(request):
    context = {'exam_manage': Exam.objects.all()}
    context2 = {'question_choice': QuestionChoice.objects.all()}
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

    

# def select_questions(request):
#     if request.method == "POST":
#         form = ExamForm(request.POST)
#         if form.is_valid():
#             form.save()
#     # form = ExamForm(request.POST)
#     # multiplechoice question algorithms
#     # if request.method == 'POST':
#         num_questions = int(request.POST.get('num_questions'))
#         questions = list(QuestionChoice.objects.all())
#         random.shuffle(questions)
#         questions = questions[:num_questions]


#         # short question algorithms
#         num_shortquestions = int(request.POST.get('num_shortquestions'))
#         questionshort = list(QuestionShortterm.objects.all())
#         random.shuffle(questionshort)
#         questionshort = questionshort[:num_shortquestions]
        
#         # long question algorithms
#         num_longquestions = int(request.POST.get('num_longquestions'))
#         questionlong = list(QuestionLongTerm.objects.all())
#         random.shuffle(questionlong)
#         questionlong = questionlong[:num_longquestions]
#         context = {
#             'questions':questions,
#             'questionshort':questionshort,
#             'questionlong':questionlong,

#         }
       
      
#         return render(request, "mtihani/generate_exam.html", context)
#     else:
       
#         # return render(request, "mtihani/generate_exam.html", context)
#         form = ExamForm()
#         return render(request, 'mtihani/add_exam.html', {"form":form})


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




# def select_questions(request):
#     if request.method == 'POST':
#         num_questions = int(request.POST.get('num_questions'))
#         questions = list(QuestionChoice.objects.all())
#         random.shuffle(questions)
#         questions = questions[:num_questions]
#         for question in questions:
#             question.save()

#         num_shortquestions = int(request.POST.get('num_shortquestions'))
#         questionshort = list(QuestionShortterm.objects.all())
#         random.shuffle(questionshort)
#         questionshort = questionshort[:num_shortquestions]
#         for question in questionshort:
#             question.save()

#         num_longquestions = int(request.POST.get('num_longquestions'))
#         questionlong = list(QuestionLongTerm.objects.all())
#         random.shuffle(questionlong)
#         questionlong = questionlong[:num_longquestions]
#         for question in questionlong:
#             question.save()

#         context = {
#             'questions':questions,
#             'questionshort':questionshort,
#             'questionlong':questionlong,

#         }
       
#         # return redirect('/matokeo')
#         return render(request, "mtihani/generate_exam.html", context)

       
#     else:
#         # form = QCategoryForm()
#         return render(request, 'mtihani/mtihani.html')

# def select_questions(request):
#     if request.method == 'POST':
#         # Retrieve the number of questions to select for each category
#         num_questions = int(request.POST.get('num_questions'))
#         num_shortquestions = int(request.POST.get('num_shortquestions'))
#         num_longquestions = int(request.POST.get('num_longquestions'))

#         # Create a new exam instance
#         exam = Exam.objects.create()

#         # Retrieve a random selection of questions from each category
#         questions = list(QuestionChoice.objects.order_by('?')[:num_questions])
#         questionshort = list(QuestionShortterm.objects.order_by('?')[:num_shortquestions])
#         questionlong = list(QuestionLongTerm.objects.order_by('?')[:num_longquestions])

#         # Add the selected questions to the exam
#         for question in questions:
#             exam_question = ExamQuestion.objects.create(exam=exam, question_choice=question)
#         for question in questionshort:
#             exam_question = ExamQuestion.objects.create(exam=exam, question_shortterm=question)
#         for question in questionlong:
#             exam_question = ExamQuestion.objects.create(exam=exam, question_longterm=question)

#         # Retrieve all ExamQuestion instances that belong to the new exam
#         exam_questions = ExamQuestion.objects.filter(exam=exam)

#         # Pass the exam_questions to the results template
#         context = {'exam_questions': exam_questions}
#         return render(request, 'mtihani/mtihani_manage.html', context)

#     else:
#         return render(request, 'mtihani/mtihani.html')








def mtihani_manage(request):
    context = {'questions': QuestionChoice.objects.all()}
    context2 = {'questionshort': QuestionShortterm.objects.all()}
    context3 = {'questionlong': QuestionLongTerm.objects.all()}
    return render(request, 'mtihani/mtihani_manage.html', {'context':context, 'context2':context2,'context3':context3})


def view_saved_questions(request):
    saved_questions = {
        'questions': QuestionChoice.objects.all(),
        'questionshort': QuestionShortterm.objects.all(),
        'questionlong': QuestionLongTerm.objects.all()
    }
    return render(request,'mtihani/mtihani_manage.html', saved_questions)    

class select_questions(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pdf1.html')
    
    def post(self, request, *args, **kwargs):
        # Retrieve num_questions, num_shortquestions, and num_longquestions values from POST request
        num_questions = int(request.POST.get('num_questions'))
        num_shortquestions = int(request.POST.get('num_shortquestions'))
        num_longquestions = int(request.POST.get('num_longquestions'))
        
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
        
        # Create a context containing the questions
        context = {
            'num_questions': num_questions,
            'num_shortquestions': num_shortquestions,
            'num_longquestions': num_longquestions,
            'questions': questions,
            'questionshort': questionshort,
            'questionlong': questionlong,
        }
        
        # Render the HTML template with the context
        html = render_to_string('pdf2.html', {'questions': questions, 'questionshort': questionshort, 'questionlong': questionlong})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="questions.pdf"'
        buffer = BytesIO()
        HTML(string=html).write_pdf(buffer)
        response.write(buffer.getvalue())

        # Return the PDF as an HTTP response
        return response