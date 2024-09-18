from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Ensure you're referencing the correct model
        fields = '__all__'  # Or specify the exact fields ['name', 'age', 'email']
