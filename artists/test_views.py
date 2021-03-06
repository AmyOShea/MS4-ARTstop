"""
Testing views in the artists app
"""

from django.test import TestCase

from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from profiles.models import User
from .models import Artist
from .forms import ArtistForm


class TestArtistsViews(TestCase):
    """
    Test views in artists app
    """
    def setUp(self):
        """
        Set up info needed for testing
        """
        self.artist1 = Artist.objects.create(
            name='artistName1',
            artist_statement='artistStatatement1',
            image='artistImage1'
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

    def test_all_artists_view(self):
        """
        Test that all users can view all artists page
        """
        response = self.client.get('/artists/')
        self.assertTemplateUsed(response, 'artists/artists.html')
        self.assertEqual(response.status_code, 200)

    def test_artist_detail_view(self):
        """
        Test that all users can view artist details page
        """
        response = self.client.get(f'/artists/{self.artist1.id}/')
        self.assertTemplateUsed(response, 'artists/artist_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_artist_view(self):
        """
        Test that only admin can access add_artist page
        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get('/artists/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get('/artists/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get('/artists/add/')
        self.assertEqual(response.status_code, 302)

    def test_edit_artist_view(self):
        """
        Test that only admin can access edit_artist page.

        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/artists/edit/{self.artist1.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get(f'/artists/edit/{self.artist1.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get(f'/artists/edit/{self.artist1.id}/')
        self.assertEqual(response.status_code, 302)

    def test_edit_artist(self):
        """
        Test that admin can edit artist

        """
        self.client.force_login(self.admin_user)
        artist = get_object_or_404(Artist, pk=self.artist1.id)
        form = ArtistForm({
            'name': 'testEditArtist',
            'artist_statement': 'testEditStatement',
            'image': 'testEditImage',
        },
            instance=artist
        )
        self.assertTrue(form.is_valid())
        form.save()
        self.client.post(f'/artists/edit/{self.artist1.id}/')
        updated_artist = Artist.objects.get(id=self.artist1.id)
        self.assertEqual(updated_artist.name, 'testEditArtist')

    def test_delete_artist_works_for_admin(self):
        """
        Test that admin can delete artist
        """
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/artists/delete/{self.artist1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Artist Deleted')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_delete_artist_doesnt_work_for_non_admin(self):
        """
        Test that non-admins cannot delete artist
        """
        self.client.force_login(self.user)
        response = self.client.get(f'/artists/delete/{self.artist1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'You are not authorized to do that.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()
