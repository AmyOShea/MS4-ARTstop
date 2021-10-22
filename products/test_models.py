"""
Testing models in the products app
"""

from django.test import TestCase
from .models import Product, Category


class TestCategoryModel(TestCase):
    """
    Test model returns category name as string
    """

    def test_string_method_returns_name(self):
        category = Category.objects.create(name='test_category_name')
        self.assertEqual(str(category), 'test_category_name')
