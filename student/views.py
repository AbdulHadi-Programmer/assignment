from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from mongoengine import ValidationError

class AddStudentView(APIView):
    def post(self, request):
        data = request.data

        try:
            # Validate required fields
            name = data.get('name')
            age = data.get('age')
            email = data.get('email')

            if not name or not age or not email:
                return Response({"error": "Name, age, and email are required fields."}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new Student instance
            student = Student(
                name=name,
                age=age,
                email=email,
                tech_skill=data.get('tech_skill', '')  # Optional field
            )

            # Save the student, which will trigger validation
            student.save()
            return Response({"message": "Student added successfully"}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            # Catch any validation errors from MongoEngine
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except KeyError as e:
            # Handle missing fields
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
