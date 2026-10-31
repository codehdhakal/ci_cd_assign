from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Page')
        
class APITestCase(TestCase):
    def test_api_hello(self):
        response = self.client.get(reverse('api-hello'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!", "status": "success"})
