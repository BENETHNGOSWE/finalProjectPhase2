# Generated by Django 4.1.7 on 2023-04-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtihani', '0010_mtihani_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtihani',
            name='modulecode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]