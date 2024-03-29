# Generated by Django 4.1 on 2024-03-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sampled_by', models.CharField(max_length=250, verbose_name='Sampled by')),
                ('unit', models.CharField(max_length=250, verbose_name='Unit')),
                ('sample_point', models.CharField(max_length=250, verbose_name='Sample Point')),
                ('sample_type', models.CharField(max_length=250, verbose_name='Sample Type')),
                ('data_time', models.DateTimeField(auto_now_add=True, verbose_name='Date Time')),
                ('hashing_name', models.CharField(max_length=250, verbose_name='Hash Name')),
            ],
        ),
    ]
