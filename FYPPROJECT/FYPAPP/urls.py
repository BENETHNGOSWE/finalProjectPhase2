from django.urls import path
from . import views
from FYPAPP import views

app_name = 'FYPAPP'

urlpatterns = [
    # path('', views.home.as_view(), name='homepage'),
    path('', views.dashboard, name='dashboard'),


    path('addcourse/', views.add_course, name='add_course'),
    path('display/', views.display, name='display'),

    path('coursedata/', views.course_manage, name='course_manage'),
    path('updatecourse/<str:pk>/', views.update_course, name="update_course"),
    path('deletecourse/<str:pk>/', views.delete_course, name="delete_course"),

    path('addmodule/', views.add_module, name='add_module'),
    path('moduledata/', views.module_manage, name='module_manage'),
    path('updatemodule/<str:pk>/', views.update_module, name="update_module"), 

    path('addquestionchoice/', views.add_question_choice, name="add_question_choice"),
    path('choice/', views.question_choice_manage, name="question_choice_manage"),
    path('short/',views.question_short_manage, name="question_short_manage"),
    # path('updatemodule/', views.update_module, name="update_module"),
   




    path('addquestion/', views.add_question, name="add_question"),
    path('addquestionchoice/', views.add_question_choice, name="add_question_choice"),
    path('addquestionshort/', views.add_question_short, name="add_question_short"),

    path('updatequestion/<str:pk>/', views.update_question, name="update_question"),
    path('updatequestionshort/<str:pk>/', views.update_question_short, name="update_question_short"),
    path('updatequestionchoice/<str:pk>/', views.update_question_choice, name="update_question_choice"),


    path('deletequestion/<str:pk>/', views.delete_question, name="delete_question"),
    path('dataA/', views.question_manage, name="question_manage"),
    path('data/', views.question_short_manage, name="question_short_manage"),
]
