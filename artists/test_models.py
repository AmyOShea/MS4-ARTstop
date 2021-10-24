"""
Testing models in the artists app
"""

from django.test import TestCase
from .models import Artist


class TestArtistsModels(TestCase):
    """
    Test artists models
    """

    def test_string_method_returns_name(self):
        """
        Test str method returns string
        """
        artist = Artist.objects.create(name='Test Name')
        self.assertEqual(str(artist), 'Test Name')
