# Generated by Django 4.1.7 on 2023-04-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtihani', '0013_remove_mtihani_examdate_remove_mtihani_examtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtihani',
            name='examdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
