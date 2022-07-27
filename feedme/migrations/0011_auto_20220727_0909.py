# Generated by Django 3.2.14 on 2022-07-27 09:09

from django.conf import settings
from django.db import migrations, models
import feedme.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedme', '0010_alter_booking_booking_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(blank=True, null=True, validators=[feedme.models.Booking.validate_date]),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'customer', 'booking_date')},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date_time',
        ),
    ]
