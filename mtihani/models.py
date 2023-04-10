from django.db import models
from FYPAPP.models import Masomo, Course, QuestionSection, QCategory, QuestionChoice, QuestionShortterm,QuestionLongTerm
# Create your models here.
class Exam(models.Model):
    examinationType = models.CharField(max_length=30,  null=True, blank=True)
    examinationName = models.CharField(max_length=30,  null=True, blank=True)
    semeter = models.IntegerField( null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True, blank=True)
    module = models.ForeignKey(Masomo, on_delete=models.CASCADE,  null=True, blank=True)
    questionChoice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, null=True, blank=True)
    questionChoice = models.ForeignKey(QuestionShortterm, on_delete=models.CASCADE, null=True, blank=True)
    questionLong = models.ForeignKey(QuestionLongTerm, on_delete=models.CASCADE, null=True, blank=True)
    # choice = models.ForeignKey(QuestionAinazote, on_delete=models.CASCADE, null=True, blank=True)
    examDuration = models.TimeField( null=True, blank=True)
    examFullmark = models.IntegerField ( null=True, blank=True)
    questionSection = models.ForeignKey(QuestionSection, on_delete=models.CASCADE,  null=True, blank=True)
    examinationDescription = models.TextField( null=True, blank=True)

    # def __str__(self):
    #     return self.examDuration

class SavedExam(models.Model):
    mtihani = models.TextField(null=True, blank=True)



class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, null=True, blank=True)
    question_shortterm = models.ForeignKey(QuestionShortterm, on_delete=models.CASCADE, null=True, blank=True)
    question_longterm = models.ForeignKey(QuestionLongTerm, on_delete=models.CASCADE, null=True, blank=True)
