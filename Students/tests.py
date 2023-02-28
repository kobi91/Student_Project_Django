from django.test import TestCase, Client
from Students.models import Student

client=Client()

class StudentRegisterTest(TestCase):
    def test_register(self):
        pass