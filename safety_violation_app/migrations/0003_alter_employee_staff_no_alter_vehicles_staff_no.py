# Generated by Django 5.2 on 2025-05-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_violation_app', '0002_alter_employee_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='staff_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='staff_no',
            field=models.CharField(max_length=100),
        ),
    ]
