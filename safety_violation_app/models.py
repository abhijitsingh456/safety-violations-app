from django.db import models

# Create your models here.
class Employee(models.Model):
    staff_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)

class Vehicles(models.Model):
    staff_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    first_vehicle = models.CharField(max_length=100, null=True)
    second_vehicle = models.CharField(max_length=100, null=True)

class SpeedViolations(models.Model):
    date = models.DateTimeField("date of violationa")
    location = models.CharField(max_length=100)
    plate_text = models.CharField(max_length=100)
    speed = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='violations')