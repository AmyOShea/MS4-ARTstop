"""
Tests views in the faqs app
"""

from django.test import TestCase


class TestFAQsViews(TestCase):
    """
    Test the faq's views
    """
    def test_page_access(self):
        """
        Test faq's page is accessible
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
