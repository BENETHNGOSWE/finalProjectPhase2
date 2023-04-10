from django.urls import path
from . import views
# from .views import create_exam

app_name = 'mtihani'

urlpatterns = [
    path('addexam/', views.add_exam, name="add_exam"),
    path('exam/', views.exam_manage, name="exam_manage"),
    path('updateexam/<str:pk>/', views.update_exam, name="update_exam"),
    path('selectquestions/', views.select_questions.as_view(), name="select_questions"),
    # path('savedexam', views.saved_exams, name="saved_exams"),
    path('pdfs/', views.GeneratePdf, name='GeneratePdf'),
    # path('generatepdf/', views.GeneratePdf, name='generate_pdf'),
    path('render', views.render_pdf_view, name="render_pdf"),
    path('list', views.ExamListView.as_view(), name="examlist"),
    path('exam/<pk>', views.exam_render_pdf, name="examrender"),


    path('matokeo/', views.mtihani_manage, name="mtihani_manage"),
    path('ona/', views.view_saved_questions, name="view_saved_questions"),
]