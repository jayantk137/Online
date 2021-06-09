# Generated by Django 3.1.2 on 2020-12-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRForm', '0002_fir_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='status',
            field=models.CharField(choices=[('Completed', ''), ('Not Updated', 'Not updated')], default='Not Updated', max_length=15),
        ),
    ]