# Generated by Django 3.1.2 on 2020-10-27 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip', models.IntegerField(max_length=8)),
                ('PoliceStation', models.CharField(max_length=64)),
                ('VicFN', models.CharField(max_length=64)),
                ('VicLN', models.CharField(max_length=64)),
                ('ComplaintType', models.CharField(max_length=64)),
                ('Description', models.TextField(max_length=64)),
                ('ComFN', models.CharField(max_length=64)),
                ('ComLN', models.CharField(max_length=64)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
