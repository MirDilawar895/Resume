# Generated by Django 4.0 on 2022-01-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_answerable_question_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerable',
            name='question_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
