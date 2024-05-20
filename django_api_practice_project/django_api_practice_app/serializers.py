from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Metal:
        model = Student
        fields = ['id', 'name', 'age', 'courses']

