# Generated by Django 5.1.4 on 2025-02-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_inherit_app', '0003_myexamcenter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myexamcenter',
            options={'ordering': ['id']},
        ),
    ]
