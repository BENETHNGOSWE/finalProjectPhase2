# Generated by Django 4.1.7 on 2023-04-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0003_remove_questionchoice_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionlongterm',
            name='answer',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionshortterm',
            name='answer',
            field=models.TextField(max_length=100),
        ),
    ]
