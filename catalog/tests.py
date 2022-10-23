from django.test import TestCase


class URLTests(TestCase):

    def test_item_list_endpoint(self):
        response = self.client.get('/catalog', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_item_detail_negative_integer_endpoint(self):
        response = self.client.get('/catalog/-1', follow=True)
        self.assertNotEqual(response.status_code, 200)

    def test_item_detail_string_endpoint(self):
        response = self.client.get('/catalog/some-string', follow=True)
        self.assertNotEqual(response.status_code, 200)

    def test_item_detail_zero_integer_endpoint(self):
        response = self.client.get('/catalog/0', follow=True)
        self.assertNotEqual(response.status_code, 200)

    def test_item_detail_positive_integer_endpoint(self):
        response = self.client.get('/catalog/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_item_detail_positive_number_endpoint(self):
        response = self.client.get('/catalog/1020', follow=True)
        self.assertEqual(response.status_code, 200)
