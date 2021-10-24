"""
Testing models in the contact app
"""

from django.test import TestCase
from .models import Contact


class TestContactModel(TestCase):
    """
    Test contact models
    """
    def test_string_method_returns_name(self):
        """ Test string methid returns string """
        name = Contact.objects.create(name='Test Name')
        self.assertEqual(str(name), 'Test Name')
