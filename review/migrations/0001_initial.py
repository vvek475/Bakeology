# Generated by Django 3.2.6 on 2021-11-05 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cake', '0002_auto_20210902_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Customer', max_length=20)),
                ('email', models.EmailField(default='customer@gmail.com', max_length=50)),
                ('mobile', models.CharField(default='Cus_Num', max_length=10)),
                ('message', models.TextField(default='Had the best cakes in the city', max_length=500)),
                ('cake', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cake.cake')),
            ],
        ),
    ]