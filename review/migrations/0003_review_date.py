# Generated by Django 3.2.6 on 2021-11-05 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 0, 33, 48, 486267)),
        ),
    ]