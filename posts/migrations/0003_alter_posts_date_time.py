# Generated by Django 3.2.6 on 2021-08-31 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210901_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]