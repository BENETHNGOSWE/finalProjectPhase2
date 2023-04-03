from django.db import models

# Create your models here.

questionsection = (
    ("YES", "YES"),
    ("NO", " NO"),
    
)
questiontype = (
    ("multichoice Questions", "multichoice Questions"),
    ("short answers Questions", "short answers Questions"),
    ("long answers Questions", "long answers Questions"),
)

questionlevel = (
    ("Normal", "Normal"),
    ("Medium", "Medium"),
    ("Hard", "Hard")
)


class Course(models.Model):
    courseName = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=30)

    def __str__(self):
        return self.courseName

class Masomo(models.Model):
    moduleName = models.CharField(max_length=30)
    moduleCode = models.CharField(max_length=30)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.moduleName

class Topic(models.Model):
    topicNumber = models.IntegerField()
    topicName = models.CharField(max_length=30)
    module = models.ForeignKey('Masomo', on_delete=models.CASCADE)
    def __str__(self):
        return self.topicName

class QuestionType(models.Model):
    questiontype = models.CharField(max_length=30)

    def __str__(self):
        return self.questiontype


class QuestionSection(models.Model):
    questionsection = models.CharField(choices=questionsection, null=True, max_length=10)

    def __str__(self):
        return self.questionsection

class QCategory(models.Model):
    questionType = models.CharField(max_length=30, null=True, blank=True, choices=questiontype)
  
    def __str__(self):
        return self.questionType


class Question(models.Model):
    questionType = models.ForeignKey(QCategory, on_delete=models.CASCADE, default='multichoice_Questions')
    questionLevel = models. CharField(max_length=30, null=True, choices=questionlevel)
    somo = models.ForeignKey('Masomo', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    questionText = models.TextField ()
    

    def __str__(self): 
        return self.questionText

class QuestionChoice(models.Model):
    question = models.CharField(max_length=100)
    category = models.ForeignKey('QCategory', on_delete=models.CASCADE, null=True, blank=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question

class QuestionShortterm(models.Model):
    category = models.ForeignKey('QCategory', on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=10)













