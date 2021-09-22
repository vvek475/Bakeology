# Generated by Django 3.2.6 on 2021-08-31 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='pic',
        ),
        migrations.AddField(
            model_name='posts',
            name='cake_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cake'),
        ),
        migrations.AddField(
            model_name='posts',
            name='customer_pic',
            field=models.ImageField(blank=True, null=True, upload_to='customers'),
        ),
        migrations.AddField(
            model_name='posts',
            name='date_time',
            field=models.DateTimeField(default='2000-12-12 12:21'),
        ),
        migrations.AddField(
            model_name='posts',
            name='review',
            field=models.TextField(default='Fine', max_length=550),
        ),
    ]