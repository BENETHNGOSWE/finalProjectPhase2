from django import forms
from .models import Exam, ExamQuestion

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'



class ExamQuestionForm(forms.ModelForm):
    class Meta:
        model = ExamQuestion
        fields = '__all__'        