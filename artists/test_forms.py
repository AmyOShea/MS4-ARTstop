"""
Testing forms in the artists app
"""

from django.test import TestCase
from .forms import ArtistForm


class TestArtistForm(TestCase):
    """
    Test that the artist form works
    """

    def test_name_is_required(self):
        """
        Test if form submits without name field
        """
        form = ArtistForm({
            'name': '',
            'artist_statement': 'test',
            'image': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_artist_statement_is_required(self):
        """
        Test if form submits without artist_statement field
        """
        form = ArtistForm({
            'name': 'test',
            'artist_statement': '',
            'image': 'test',
        })
        # Form should not be valid - srtist statement required
        self.assertFalse(form.is_valid())
        self.assertIn('artist_statement', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['artist_statement'][0], 'This field is required.')

    def test_image_is_required(self):
        """
        Test if form submits without image field
        """
        form = ArtistForm({
            'name': 'test',
            'artist_statement': 'test',
            'image': '',
        })
        # Form should not be valid - image required
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['image'][0], 'This field is required.')
