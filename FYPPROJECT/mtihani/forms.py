from django import forms
from .models import Exam,Mtihani

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'



class MtihaniForm(forms.ModelForm):
    # examdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Mtihani
        fields = '__all__'        