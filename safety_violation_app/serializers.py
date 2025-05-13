from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'

class NoOfSpeedViolationSerializer(serializers.Serializer):
    staff_no = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    designation = serializers.CharField(max_length=100)
    no_of_violations = serializers.CharField(max_length=100)
