from django.urls import path
from .views import StudentCreateView

urlpatterns = [
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
]