from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, ShopImage

# Create your tests here.

class ProductTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(name='Cat1')
        self.category2 = Category.objects.create(name='Cat2')
        self.product1 = Product.objects.create(name='Prod1', description='desc1', price=10, category=self.category1)
        self.product2 = Product.objects.create(name='Prod2', description='desc2', price=20, category=self.category2)
        self.shop_image = ShopImage.objects.create(title='Gallery', image=None)

    def test_product_list_shows_products(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prod1')
        self.assertContains(response, 'Prod2')

    def test_product_list_category_filter(self):
        response = self.client.get(reverse('product_list'), {'category': self.category1.id})
        self.assertContains(response, 'Prod1')
        self.assertNotContains(response, 'Prod2')

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prod1')
