"""
Test models in checkout app
"""

from django.test import TestCase
from django.conf import settings

from products.models import Product
from .models import Order


class TestOrderModels(TestCase):
    """
    Test that order models work correctly
    """

    def setUp(self):
        Order.objects.create(
            full_name='test test',
            email='test@test.com',
            phone_number='0123456789',
            street_address1='test',
            town_or_city='test',
            country='IE'
        )

    def test_order_string_method_returns_order_number(self):
        """
        Test string method for Order class
        """
        order_number = Order.objects.create(order_number='2000')
        self.assertEqual(str(order_number), '2000')
