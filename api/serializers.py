from rest_framework import serializers
from myapp.models import employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'