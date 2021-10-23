"""
This module tests the views in the checkout app
"""

from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from products.models import Product, Category


class TestCheckoutViews(TestCase):
    """
    Test that the checkout works properly
    """

    def test_cache_checkout_data(self):
        """
        Test that the cache_checkout_data function responds correctly
        """
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

    def test_the_checkout_page_url_exists(self):
        """
        Test that the checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_nothing_in_bag_error(self):
        """
        Test that an error message is shown when nothing is in the shopping bag
        """
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "Your bag is empty")
