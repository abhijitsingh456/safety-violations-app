# Generated by Django 5.2 on 2025-05-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('email_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('first_vehicle', models.CharField(max_length=100)),
                ('second_vehicle', models.CharField(max_length=100)),
            ],
        ),
    ]
