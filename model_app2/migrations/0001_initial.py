# Generated by Django 5.1.4 on 2025-02-14 11:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('page_name', models.CharField(max_length=70)),
                ('page_cate', models.CharField(max_length=70)),
                ('page_publish_date', models.DateField()),
            ],
        ),
    ]
