# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicalPractice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[(datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '8 AM'), (datetime.time(10, 0), '8 AM'), (datetime.time(11, 0), '8 AM'), (datetime.time(12, 0), '8 AM'), (datetime.time(13, 0), '8 AM'), (datetime.time(14, 0), '8 AM'), (datetime.time(15, 0), '8 AM'), (datetime.time(16, 0), '8 AM'), (datetime.time(17, 0), '8 AM'), (datetime.time(18, 0), '8 AM'), (datetime.time(19, 0), '8 AM')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalPractice.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalPractice.Patient')),
            ],
        ),
    ]
