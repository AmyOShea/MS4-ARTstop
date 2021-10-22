"""
Testing models in the classes app
"""

from django.test import TestCase
from .models import Class, Level


class TestLevelModel(TestCase):

    def test_string_method_returns_name(self):
        level = Class.objects.create(name='test_level_name')
        self.assertEqual(str(level), 'test_level_name')

class TestClassModel(TestCase):

    def test_string_method_returns_name(self):
        a_class = Class.objects.create(name='Test Class Name')
        self.assertEqual(str(a_class), 'Test Class Name')
