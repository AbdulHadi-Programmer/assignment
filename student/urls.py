# urls.py in your Django app
from django.urls import path
from .views import *

# urlpatterns = [
#     path('add_student/', StudentView.as_view(), name='student_api'),  # URL for the API view
#     path('students/', student_list, name='student_list'),  # URL for the HTML rendering view
# ]
from django.urls import path
from .views import AddStudentView

urlpatterns = [
    path('add_student/', AddStudentView.as_view(), name='add_student'),
]
