from django.test import TestCase
from catalog.models import Category, Item, Tag
from django.core.exceptions import ValidationError


# Testing catalog.urls
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
            with self.subTest(f'Item in catalog with {case} index'):
                response = self.client.get(f'/catalog/{case}/')
                self.assertEqual(response.status_code, result)


'''
# Testing catalog.models.Category
class CategoryModelTests(TestCase):
    def test_unable_create_category(self):
        cases = ['sdf/asd', '1!asda', '$@#asd', 'ASD%1']
        for case in cases:
            with self.subTest('Create category with slug = "{case}"'):
                with self.assertRaises(ValidationError):
                    category = Item(
                        name='Тестовая категория'
                    )
                    category.full_clean()

    def test_create_category(self):
        cases = ['sdfasd', '1asda', 'asd', 'ASD1']
        for case in cases:
            with self.subTest('Can\'t create category with slug = "{case}"'):
                with self.assertRaises(ValidationError):
                    category = Item(
                        name='Тестовая категория'
                    )
                    category.full_clean()
'''


# Testing catalog.models.Item
class ItemModelTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug'
        )
        cls.tag = Tag.objects.create(
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    def test_unable_create_item(self):
        cases = ['превосходно', 'роскошно',
                 'роскошнопревосходно', 'тестовое описание товара']
        for case in cases:
            with self.subTest(f'Create item with text = "{case}"'):
                with self.assertRaises(ValidationError):
                    item = Item(
                        name='Тестовый айтем',
                        category=self.category,
                        text=case
                    )
                    item.full_clean()

    def test_create_item(self):
        cases = ['превосходно описанный товар', 'роскошно описанный товар']
        for case in cases:
            with self.subTest(f'Can\'t create item with text = "{case}"'):
                item = Item(
                        name='Тестовый айтем',
                        category=self.category,
                        text=case
                    )
                item.full_clean()
