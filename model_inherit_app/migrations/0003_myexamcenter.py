# Generated by Django 5.1.4 on 2025-02-14 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_inherit_app', '0002_examcenter_student1'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('model_inherit_app.examcenter',),
        ),
    ]
