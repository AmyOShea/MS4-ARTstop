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

    def test_checkout_details(self):
        """
        Test that the checkout fields auto-fill from the user info
        """
        order = Order.objects.get(id=1)

        self.assertEqual(order.full_name, 'test test')
        self.assertEqual(order.email, 'test@test.com')
        self.assertEqual(order.phone_number, '0123456789')
        self.assertEqual(order.street_address1, 'test')
        self.assertEqual(order.country, 'IE')

    def test_update_total(self):
        """
        Test that the order total is updated correctly
        """

        delivery = settings.STANDARD_DELIVERY
        # test delivery charge when total < free delivery threshold
        order_total = 10
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = delivery
            self.assertEqual(delivery_cost, 15)
        else:
            delivery_cost = 0
            self.assertEqual(delivery_cost, 0)

        grand_total = order_total + delivery_cost
        self.assertEqual(grand_total, 25)

        # test delivery charge when total > free delivery threshold
        order_total = 90
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = delivery
            self.assertEqual(delivery_cost, 15)
        else:
            delivery_cost = 0
            self.assertEqual(delivery_cost, 0)

        grand_total = order_total + delivery_cost
        self.assertEqual(grand_total, 90)


class TestOrderLineItemModels(TestCase):
    """
    Test order models work correctly
    """

    def test_order_line_item_string_method(self):
        """
        Test string method for OrderLineItem
        """
        product = Product.objects.create(sku='1', price=60)
        order = Order.objects.create(order_number='1234')
        expected_output = 'SKU 1 on order 1234'
        self.assertEqual(str(
            f'SKU {product.sku} on order {order.order_number}'),
            expected_output)
