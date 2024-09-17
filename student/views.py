from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentCreateView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            # return Response(StudentSerializer(student).data, status=201)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)