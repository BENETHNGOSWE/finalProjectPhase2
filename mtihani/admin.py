from django.contrib import admin
from .models import Exam, SavedExam, ExamQuestion
# Register your models here.
admin.site.register(Exam)
admin.site.register(SavedExam)
admin.site.register(ExamQuestion)


