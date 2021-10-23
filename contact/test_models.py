"""
Testing models in the contact app
"""

from django.test import TestCase
from .models import Contact


class TestContactModel(TestCase):

    def test_string_method_returns_name(self):
        name = Contact.objects.create(name='Test Name')
        self.assertEqual(str(name), 'Test Name')
