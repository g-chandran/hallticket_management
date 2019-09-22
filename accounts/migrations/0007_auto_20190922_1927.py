# Generated by Django 2.2.1 on 2019-09-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_studentexam_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinerprofile',
            name='staffid',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='rollno',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.DeleteModel(
            name='StudentExam',
        ),
    ]
