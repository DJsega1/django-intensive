from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):

    def test_homepage_endpoint(self):
        response = self.client.get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    fixtures = ['fixtures/catalog.json', ]

    def test_home_page_show_correct_context(self):
        response = self.client.get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 2)
