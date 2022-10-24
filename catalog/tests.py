from django.test import TestCase


class URLTests(TestCase):

    def test_item_list_endpoint(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):

        with self.subTest("Item in catalog with negative integer index"):
            response = self.client.get('/catalog/-1/')
            self.assertEqual(response.status_code, 404)

        with self.subTest("Item in catalog with string index"):
            response = self.client.get('/catalog/some-string/')
            self.assertEqual(response.status_code, 404)

        with self.subTest("Item in catalog with zero index"):
            response = self.client.get('/catalog/0/')
            self.assertEqual(response.status_code, 404)

        with self.subTest("Item in catalog with float index"):
            response = self.client.get('/catalog/1.2/')
            self.assertEqual(response.status_code, 404)

        with self.subTest("Item in catalog with correct index"):
            response = self.client.get('/catalog/1203/')
            self.assertEqual(response.status_code, 200)
