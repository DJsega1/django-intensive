from django.test import TestCase


class URLTests(TestCase):

    def test_item_list_endpoint(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        cases = {
            -1: 404,
            0: 404,
            1.2: 404,
            "some_string": 404,
            1203: 200
        }
        for case, result in cases.items():
            with self.subTest(f"Item in catalog with {case} index"):
                response = self.client.get(f'/catalog/{case}/')
                self.assertEqual(response.status_code, result)
