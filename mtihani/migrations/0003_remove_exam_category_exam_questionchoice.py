# Generated by Django 4.1.7 on 2023-03-31 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0002_questionchoice'),
        ('mtihani', '0002_exam_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='category',
        ),
        migrations.AddField(
            model_name='exam',
            name='questionChoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.questionchoice'),
        ),
    ]
