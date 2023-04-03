from django import forms
from .models import Masomo, Question, Course, QCategory,QuestionChoice


class MasomoForm(forms.ModelForm):
    class Meta:
        model = Masomo
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class QCategoryForm(forms.ModelForm):
    class Meta:
        model = QCategory
        fields = '__all__'      

class QuestionChoiceForm(forms.ModelForm):
    class Meta:
        model = QuestionChoice
        fields = '__all__'

        
# class QuestionForm(models.Model):
#     questiontype = models.ForeignKey('QuestionType', on_delete=models.CASCADE)
#     questionLevel = models. ForeignKey('QuestionLevel', on_delete=models.CASCADE)
#     somo = models.ForeignKey('Masomo', on_delete=models.CASCADE)
#     topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
#     questionText = models.TextField ()
    