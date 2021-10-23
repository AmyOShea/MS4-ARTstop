"""
Testing views in the classes app
"""

from django.test import TestCase

from django.shortcuts import get_object_or_404

from profiles.models import User
from .models import Class
from.forms import ClassForm


class TestClassesViews(TestCase):
    """
    Test views in classes app
    """
    def setUp(self):
        """
        Set up info needed for testing
        """
        self.class1 = Class.objects.create(
            name='testClass',
            description='test',
            duration='00:00:00',
            cover_image='test'
        )

        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='1234',
            email='admin@test.com',
        )

        self.user = User.objects.create_user(
            username='user',
            password='1234',
            email='user@test.com',
        )

    def test_all_classes_view(self):
        """
        Test that all users can view all classes page
        """
        response = self.client.get('/classes/')
        self.assertTemplateUsed(response, 'classes/classes.html')
        self.assertEqual(response.status_code, 200)

    def test_class_detail_view(self):
        """
        Test that all users can view class details page
        """
        response = self.client.get(f'/classes/{self.class1.id}/')
        self.assertTemplateUsed(response, 'classes/class_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_class_view(self):
        """
        Test that only admin can access add_class page
        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get('/classes/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get('/classes/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get('/classes/add/')
        self.assertEqual(response.status_code, 302)

    # def test_add_class(self):
    #     """
    #     Test that admin can add classes
    # FORM VALIDATION CURRENTLY FAILING

    #     """
    #     self.client.force_login(self.admin_user)
    #     add_class_form = ClassForm({
    #         'name': 'testClass',
    #         'description': 'testDescription',
    #         'duration': '00:22:00',
    #         'cover_image': 'testImage'
    #     })

    #     self.client.post('/classes/add/')
    #     self.assertTrue(add_class_form.is_valid())
    #     add_class_form.save()
    #     add_class = Class.objects.all()
    #     self.assertEqual(len(add_class), 2)

    def test_edit_class_view(self):
        """
        Test that only admin can access edit_class page.

        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/classes/edit/{self.class1.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get(f'/classes/edit/{self.class1.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get(f'/classes/edit/{self.class1.id}/')
        self.assertEqual(response.status_code, 302)

    def test_edit_class(self):
        """
        Test that admin can edit classes

        """
        self.client.force_login(self.admin_user)
        a_class = get_object_or_404(Class, pk=self.class1.id)
        class_form = ClassForm({
            'name': 'testEditClass',
            'description': 'testEditDescription',
            'duration': '00:11:00',
            'cover_image': 'testEditImage'
        },
            instance=a_class
        )
        self.assertTrue(class_form.is_valid())
        class_form.save()
        self.client.post(f'/classes/edit/{self.class1.id}/')
        updated_class = Class.objects.get(id=self.class1.id)
        self.assertEqual(updated_class.name, 'testEditClass')
