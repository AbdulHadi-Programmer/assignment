from django.db import models
from mongoengine import Document, StringField, IntField, EmailField

class Student(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)
    email = EmailField(required=True)
    tech_skill = StringField(max_length=200)

    def __str__(self):
        return self.name