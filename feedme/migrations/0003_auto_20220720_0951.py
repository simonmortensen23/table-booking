# Generated by Django 3.2.14 on 2022-07-20 09:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedme', '0002_auto_20220719_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=cloudinary.models.CloudinaryField(default='Placeholder', max_length=255, verbose_name='image'),
        ),
    ]
