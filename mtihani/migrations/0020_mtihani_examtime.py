# Generated by Django 4.1.7 on 2023-04-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtihani', '0019_alter_mtihani_semeter'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtihani',
            name='examtime',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
