from django.contrib import admin
from .models import Course,QuestionChoice, Masomo, Question, Topic, QuestionSection, QCategory, QuestionShortterm, QuestionLongTerm

# Register your models here.
admin.site.register(Course)
admin.site.register(Masomo)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(QuestionSection)
admin.site.register(QCategory)
admin.site.register(QuestionChoice)
admin.site.register(QuestionShortterm)
admin.site.register(QuestionLongTerm)