from django.db import models
from FYPAPP.models import Masomo, Course, QuestionSection
# Create your models here.
class Exam(models.Model):
    examinationType = models.CharField(max_length=30)
    examinationName = models.CharField(max_length=30)
    semeter = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Masomo, on_delete=models.CASCADE)
    examDuration = models.TimeField()
    examFullmark = models.IntegerField ()
    questionSection = models.ForeignKey(QuestionSection, on_delete=models.CASCADE)
    examinationDescription = models.TextField()

    # def __str__(self):
    #     return self.examDuration