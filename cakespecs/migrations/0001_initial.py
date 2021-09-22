# Generated by Django 3.2.6 on 2021-09-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cakespecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cake_name', models.CharField(default='Call', max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('email', models.EmailField(default='demo@gmail.com', max_length=100)),
                ('mob_number', models.CharField(default='+91 99999 99999', max_length=15)),
                ('toppins', models.CharField(default='None', max_length=100)),
                ('message', models.CharField(default='None', max_length=100)),
                ('additionals', models.CharField(max_length=25)),
            ],
        ),
    ]