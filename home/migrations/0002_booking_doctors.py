# Generated by Django 5.0.6 on 2024-07-16 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=10)),
                ('p_email', models.CharField(max_length=100)),
                ('dep_name', models.CharField(max_length=100)),
                ('doc_name', models.CharField(max_length=100)),
                ('booking_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]