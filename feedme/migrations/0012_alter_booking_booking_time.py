# Generated by Django 3.2.14 on 2022-07-27 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedme', '0011_auto_20220727_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(choices=[(datetime.time(7, 0), '7:00 am'), (datetime.time(8, 0), '8:00 am'), (datetime.time(9, 0), '9:00 am'), (datetime.time(18, 0), '6:00 pm'), (datetime.time(19, 0), '7:00 pm'), (datetime.time(20, 0), '8:00 pm'), (datetime.time(21, 0), '9:00 pm')], null=True),
        ),
    ]