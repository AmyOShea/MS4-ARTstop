"""
Testing models in the products app
"""

from django.test import TestCase
from .models import Category


class TestCategoryModel(TestCase):
    """
    Test category model returns category name as string
    """

    def test_string_method_returns_name(self):
        """
        Test model returns category name as string
        """
        category = Category.objects.create(name='test_category_name')
        self.assertEqual(str(category), 'test_category_name')
