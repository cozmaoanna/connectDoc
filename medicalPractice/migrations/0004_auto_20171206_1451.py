# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicalPractice', '0003_remove_medicalpractice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='practice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='medicalPractice.MedicalPractice'),
        ),
    ]
