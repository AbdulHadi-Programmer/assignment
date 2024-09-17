from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        from .models import Student
        student = Student(**validated_data)
        student.save()
        return student
