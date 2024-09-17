from django.urls import path
from .views import StudentListCreate

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
]
