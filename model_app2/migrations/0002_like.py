# Generated by Django 5.1.4 on 2025-02-14 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='model_app2.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('model_app2.page',),
        ),
    ]
