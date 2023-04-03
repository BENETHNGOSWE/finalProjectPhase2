from django.urls import path
from . import views
# from .views import create_exam

app_name = 'mtihani'

urlpatterns = [
    path('addexam/', views.add_exam, name="add_exam"),
    path('exam/', views.exam_manage, name="exam_manage"),
    path('updateexam/<str:pk>/', views.update_exam, name="update_exam"),

]