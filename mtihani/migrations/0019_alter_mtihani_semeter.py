# Generated by Django 4.1.7 on 2023-04-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtihani', '0018_mtihani_examinationdescription2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtihani',
            name='semeter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
