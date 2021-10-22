"""
Testing forms in the checkout app
"""

from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test that the order form works
    """

    def test_full_name_is_required(self):
        """
        Test if form submits without full_name field
        """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'ie',
        })
        # Form should not be valid - full_name required
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Test if form submits without email field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'ie',
        })
        # Form should not be valid - email is required
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        Test if form submits without phone_number
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'ie',
        })
        # Form should not be valid - phone_number required
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test if form submits without country field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': '',
        })
        # Form should not be valid - country is required
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        """
        Test if form submits without town_or_city field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'country': 'ie',
            'town_or_city': '',
            'street_address1': 'test',
        })
        # Form should not be valid - town_or_city is required
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        """
        Test if form submits without street_address1 field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': '',
            'town_or_city': 'test',
            'country': 'ie',
        })
        # Form should not be valid - street_address1 is required
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_fields_are_correct_in_meta_class(self):
        """
        Check that the correct form fields are visible to user
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'county', 'postcode',
            'country'
        ))
