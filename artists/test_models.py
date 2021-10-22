"""
Testing models in the artists app
"""

from django.test import TestCase
from .models import Artist


class TestModels(TestCase):

    def test_string_method_returns_name(self):
        artist = Artist.objects.create(name='Test Name')
        self.assertEqual(str(artist), 'Test Name')
