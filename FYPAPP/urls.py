from django.urls import path
from . import views
from FYPAPP import views

app_name = 'FYPAPP'

urlpatterns = [
    path('', views.home.as_view(), name='homepage'),
    path('dashboard/', views.dashboard.as_view(), name='dashboard'),


    path('addcourse/', views.add_course, name='add_course'),
    path('coursedata/', views.course_manage, name='course_manage'),
    path('updatecourse/<str:pk>/', views.update_course, name="update_course"),
    path('deletecourse/<str:pk>/', views.delete_course, name="delete_course"),

    path('addmodule/', views.add_module, name='add_module'),
    path('moduledata/', views.module_manage, name='module_manage'),
    path('updatemodule/<str:pk>/', views.update_module, name="update_module"), 

    # path('addmodule/', views.add_module, name="add_module"),
    # path('moduledata/', views.module_manage, name="module_manage"),
    # path('updatemodule/', views.update_module, name="update_module"),
   




    path('addquestion/', views.add_question, name="add_question"),
    path('updatequestion/<str:pk>/', views.update_question, name="update_question"),
    path('deletequestion/<str:pk>/', views.delete_question, name="delete_question"),
    path('data/', views.question_manage, name="question_manage"),
]
