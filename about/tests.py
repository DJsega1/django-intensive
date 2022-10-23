from django.test import TestCase


class URLTests(TestCase):

    def test_description_endpoint(self):
        response = self.client.get('/about', follow=True)
        self.assertEqual(response.status_code, 200)
