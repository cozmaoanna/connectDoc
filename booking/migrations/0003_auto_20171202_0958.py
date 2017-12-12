# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 09:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20171201_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[(datetime.time(8, 0), '8:00 AM'), (datetime.time(8, 15), '8:15 AM'), (datetime.time(8, 30), '8:30 AM'), (datetime.time(8, 45), '8:45 AM'), (datetime.time(9, 0), '9:00 AM'), (datetime.time(9, 15), '9:15 AM'), (datetime.time(9, 30), '9:30 AM'), (datetime.time(9, 45), '9:45 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 15), '10:15 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(10, 45), '10:45 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 15), '11:15 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(11, 45), '11:45 AM'), (datetime.time(12, 0), '12:00 AM'), (datetime.time(12, 15), '12:15 AM'), (datetime.time(12, 30), '12:30 AM'), (datetime.time(12, 45), '12:45 AM'), (datetime.time(13, 0), '1:00 PM'), (datetime.time(13, 15), '1:15 PM'), (datetime.time(13, 30), '1:30 PM'), (datetime.time(13, 45), '1:45 PM'), (datetime.time(14, 0), '2:00 PM'), (datetime.time(14, 15), '2:15 PM'), (datetime.time(14, 30), '2:30 PM'), (datetime.time(14, 45), '2:45 PM'), (datetime.time(15, 0), '3:00 PM'), (datetime.time(15, 15), '3:15 PM'), (datetime.time(15, 30), '3:30 PM'), (datetime.time(15, 45), '3:45 PM'), (datetime.time(16, 0), '4:00 PM'), (datetime.time(16, 15), '4:15 PM'), (datetime.time(16, 30), '4:30 PM'), (datetime.time(16, 45), '4:45 PM'), (datetime.time(17, 0), '5:00 PM'), (datetime.time(17, 15), '5:15 PM'), (datetime.time(17, 30), '5:30 PM'), (datetime.time(17, 45), '5:45 PM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(18, 15), '6:15 PM'), (datetime.time(18, 30), '6:30 PM'), (datetime.time(18, 45), '6:45 PM'), (datetime.time(19, 0), '7:00 PM'), (datetime.time(19, 15), '7:15 PM'), (datetime.time(19, 30), '7:30 PM'), (datetime.time(19, 45), '7:45 PM')]),
        ),
    ]