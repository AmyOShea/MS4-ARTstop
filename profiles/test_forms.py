"""
Testing forms in the profiles app
"""

from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Test that the profile form works
    """

    def test_fields_are_not_required(self):
        """
        Test if form submits without any fields
        """
        form_info = {
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_county': '',
            'default_postcode': '',
        }
        form = UserProfileForm(data=form_info)
        # Form should be valid - no fields required
        self.assertTrue(form.is_valid())
        # Check there are no error messages
        self.assertFalse(form.errors)
