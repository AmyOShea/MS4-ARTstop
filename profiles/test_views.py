"""
Test profiles apps views
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from checkout.models import Order
from .models import UserProfile


class TestProfilesViews(TestCase):
    """
    Test profiles page views
    """
    def setUp(self):
        """
        Set up info needed for testing
        """

        self.test_user = User.objects.create_user(
            username='test',
            email='test@test.com',
            password='0123',
        )

        self.test_user_profile = get_object_or_404(UserProfile,
                                                   user=self.test_user)

    def test_profile_view(self):
        """
        Test that user can access profile page when logged in
        """

        # Check page loads if user logged in
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')
        self.client.logout()

        # # Check page redirects if user not logged in
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('accounts/login/')

    def test_default_delivery_information_updates(self):
        """
        Test that default delivery info updates
        """
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

        new_data = {
            'default_phone_number': 'testEdit',
            'default_street_address1': 'testEdit',
            'default_town_or_city': 'testEdit',
            'default_postcode': 'testEdit',
            'default_county': 'testEdit',
            'default_country': 'IE'
        }
        self.client.post('/profile/', new_data)
        response = self.client.post('/profile/', new_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Delivery Information Updated!')
        self.client.logout()

    def test_order_history_displays(self):
        """
        Test that the order history is viewable
        """
        self.client.force_login(self.test_user)

        Order.objects.create(
            order_number='123'
        )
        order_number = '123'
        response = self.client.get(
            f'/profile/order_history/{order_number}/')
        self.assertTemplateUsed(
            response, template_name="checkout/checkout_success.html")
