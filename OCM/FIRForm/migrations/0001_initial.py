# Generated by Django 3.1.2 on 2020-11-08 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip', models.PositiveIntegerField()),
                ('PoliceStation', models.CharField(max_length=64)),
                ('VicFN', models.CharField(max_length=64)),
                ('VicLN', models.CharField(max_length=64)),
                ('ComplaintType', models.CharField(max_length=64)),
                ('Description', models.TextField()),
                ('ComFN', models.CharField(max_length=64)),
                ('ComLN', models.CharField(max_length=64)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]