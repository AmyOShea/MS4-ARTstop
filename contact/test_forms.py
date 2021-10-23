"""
Testing forms in the contact app
"""

from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    Test that the contact form works
    """

    def test_name_is_required(self):
        """
        Test if form submits without name field
        """
        form = ContactForm({
            'name': '',
            'contact_email': 'test@test.com',
            'contact_as': 'test',
            'message': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_contact_email_is_required(self):
        """
        Test if form submits without contact_email field
        """
        form = ContactForm({
            'name': 'test',
            'contact_email': '',
            'contact_as': 'test',
            'message': 'test',
        })
        # Form should not be valid - contact_email required
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['contact_email'][0], 'This field is required.')

    def test_contact_as_is_required(self):
        """
        Test if form submits without contact_as field
        """
        form = ContactForm({
            'name': 'test',
            'contact_email': 'test@test.com',
            'contact_as': '',
            'message': 'test',
        })
        # Form should not be valid - contact_as required
        self.assertFalse(form.is_valid())
        self.assertIn('contact_as', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['contact_as'][0], 'This field is required.')

    def test_message_is_required(self):
        """
        Test if form submits without message field
        """
        form = ContactForm({
            'name': 'test',
            'contact_email': 'test@test.com',
            'contact_as': 'test',
            'message': '',
        })
        # Form should not be valid - message required
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['message'][0], 'This field is required.')

