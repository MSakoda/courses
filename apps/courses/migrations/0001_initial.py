# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
