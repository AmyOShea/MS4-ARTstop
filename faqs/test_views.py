"""
This module tests the views in the home app
"""

from django.test import TestCase


class TestFAQsViews(TestCase):
    """
    Test the faq's views
    """
    def test_page_access(self):
        """
        Test faq page is accessible
        """
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
