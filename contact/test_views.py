"""
Test contact apps views
"""

from django.test import TestCase

from django.contrib.messages import get_messages


class TestContactViews(TestCase):
    """
    Test contact page views
    """

    def test_contact_us_view(self):
        """
        Test that contact page is accessible
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_form(self):
        """
        Test that contact form is sent
        """
        name = 'test name'
        email = 'test@test.com'
        contact_as = 'test'
        message = 'test message'

        data = {
            'name': name,
            'contact_email': email,
            'contact_as': contact_as,
            'message': message
        }

        response = self.client.post('/contact/', data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Mail Sent!')
