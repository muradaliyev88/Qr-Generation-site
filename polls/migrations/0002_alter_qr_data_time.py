# Generated by Django 4.1 on 2024-03-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='data_time',
            field=models.DateTimeField(verbose_name='Date Time'),
        ),
    ]
