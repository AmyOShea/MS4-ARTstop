"""
Testing forms in the classes app
"""

from django.test import TestCase
from .forms import ClassForm
from .models import Class


class TestClassForm(TestCase):
    """
    Test that the class form works
    """

    def test_name_is_required(self):
        """
        Test if form submits without name field
        """
        form = ClassForm({
            'name': '',
            'description': 'test',
            'duration': 'test',
            'cover_image': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        """
        Test if form submits without description field
        """
        form = ClassForm({
            'name': 'test',
            'description': '',
            'duration': 'test',
            'cover_image': 'test',
        })
        # Form should not be valid - description required
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_duration_is_required(self):
        """
        Test if form submits without duration field
        """
        form = ClassForm({
            'name': 'test',
            'description': 'test',
            'duration': '',
            'cover_image': 'test',
        })
        # Form should not be valid - duration required
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['duration'][0], 'This field is required.')

    def test_cover_image_is_required(self):
        """
        Test if form submits without cover_image field
        """
        form = ClassForm({
            'name': 'test',
            'description': 'test',
            'duration': 'test',
            'cover_image': '',
        })
        # Form should not be valid - cover_image required
        self.assertFalse(form.is_valid())
        self.assertIn('cover_image', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['cover_image'][0], 'This field is required.')
