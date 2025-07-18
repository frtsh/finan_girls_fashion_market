from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_list_page_loads(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fashion Blog')
