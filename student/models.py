from mongoengine import Document, fields

class Student(Document):
    name = fields.StringField(required=True)
    age = fields.IntField(required=True)
    email = fields.EmailField(required=True)
