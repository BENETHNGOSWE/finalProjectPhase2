# Generated by Django 4.1.7 on 2023-04-01 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0004_questionchoice_category'),
        ('mtihani', '0004_exam_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.questionainazote'),
        ),
    ]