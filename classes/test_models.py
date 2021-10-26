"""
Testing models in the classes app
"""

from django.test import TestCase
from .models import Class, Level


class TestLevelModel(TestCase):
    """
    Test level model
    """

    def test_string_method_returns_name(self):
        """ Test level name returns as string """
        level = Level.objects.create(name='test_level_name',
                                     friendly_name='Test level name')
        self.assertEqual(str(level), 'test_level_name')
        self.assertEqual(level.get_friendly_name(), 'Test level name')


class TestClassModel(TestCase):
    """
    Test Class model
    """

    def test_string_method_returns_name(self):
        """ Test class name returns as string """
        a_class = Class.objects.create(name='Test Class Name')
        self.assertEqual(str(a_class), 'Test Class Name')
