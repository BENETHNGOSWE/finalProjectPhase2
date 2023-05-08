from django.db import models
from FYPAPP.models import Masomo, Course, QuestionSection, QCategory, QuestionChoice, QuestionShortterm,QuestionLongTerm
import datetime
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



class Mtihani(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True, blank=True)
    module = models.ForeignKey(Masomo, on_delete=models.CASCADE,  null=True, blank=True)
    modulecode = models.CharField(max_length=50, null=True, blank=True)
    semeter = models.CharField(max_length=50, null=True, blank=True)
    exam_name = models.CharField(max_length=50)
    examdate = models.DateField(null=True)
    examtime = models.CharField(max_length=50, null=True, blank=True)
    examinationDescription = models.CharField(max_length=300, null=True, blank=True)
    examinationDescription2 = models.CharField(max_length=300, null=True, blank=True)
    examinationDescription3 = models.CharField(max_length=300, null=True, blank=True)
    num_questions = models.IntegerField()
    num_shortquestions = models.IntegerField()
    num_longquestions = models.IntegerField()