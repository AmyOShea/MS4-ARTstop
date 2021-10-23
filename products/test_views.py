"""
Testing views in the products app
"""

from django.test import TestCase

from django.shortcuts import get_object_or_404

from profiles.models import User
from .models import Product, Category
from .forms import ProductForm


class TestProductsViews(TestCase):
    """
    Test views in products app
    """
    def setUp(self):
        """
        Set up info needed for testing
        
        """

        self.category1 = Category.objects.create(
            name='testCategory',
            friendly_name='TestCategory',
        )

        self.product1 = Product.objects.create(
            category=self.category1,
            name='testProduct',
            description='test',
            price='75',
            image='test'
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

    def test_all_products_view(self):
        """
        Test that all users can view all products page
        """
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """
        Test that all users can view product details page
        """
        response = self.client.get(f'/products/{self.product1.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_product_view(self):
        """
        Test that only admin can access add_product page
        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    # def test_add_product(self):
    #     """
    #     Test that admin can add products
    # FORM VALIDATION CURRENTLY FAILING

    #     """
    #     self.client.force_login(self.admin_user)
    #     add_product_form = ProductForm({
    #         'category': self.category1.pk,
    #         'name': 'testAddProduct',
    #         'description': 'testAddDescription',
    #         'price': '75',
    #         'image': 'testAddImage'
    #     })

    #     self.client.post('/products/add/')
    #     self.assertTrue(add_product_form.is_valid())
    #     add_product_form.save()
    #     add_product = Product.objects.all()
    #     self.assertEqual(len(add_product), 2)

    def test_edit_product_view(self):
        """
        Test that only admin can access edit_product page.

        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product(self):
        """
        Test that admin can edit products

        """
        self.client.force_login(self.admin_user)
        product = get_object_or_404(Product, pk=self.product1.id)
        product_form = ProductForm({
            'category': self.category1.pk,
            'name': 'testEditProduct',
            'description': 'testEditDescription',
            'price': '100',
            'image': 'testEditImage'
        },
            instance=product
        )
        self.assertTrue(product_form.is_valid())
        product_form.save()
        self.client.post(f'/products/edit/{self.product1.id}/')
        updated_product = Product.objects.get(id=self.product1.id)
        self.assertEqual(updated_product.name, 'testEditProduct')
