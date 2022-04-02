from itertools import count
from unicodedata import name
from django.test import TestCase

from shop.models import(
    Product,
    Category, 
    Reviews, 
    Rating, 
    RatingStar, 
    ProductShots, 
    Brand, 
    OperatingSystems, 
    Platform, 
    Ram
    )

class CategoryModelTestCase(TestCase):
    """Тест категорий"""

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(
            name='Сихофазатроны', slug='sihofazatroni'
        )

    def test_first_name(self):
        category = Category.objects.first()
        self.assertEqual(str(category), 'Сихофазатроны')

    def test_book_absolute_url_with_200(self):
        category = Category.objects.first()
        self.assertEqual(category.get_absolute_url(), '/shop/sihofazatroni')
        response = self.client.get(category.get_absolute_url())
        self.assertEqual(response.status_code, 200)


class ProductModelTestCase(TestCase):
    """Тест продукта"""
    
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Категория')
        brand = Brand.objects.create(name='Opple')
        os = OperatingSystems.objects.create(name='Ondroid')
        platform = Platform.objects.create(name='Ondro')
        ram = Ram.objects.create(count=1)
        product = Product.objects.create(
            category=category,
            name='Product',
            slug='product',
            description='product123',
            price=1010,
            stock=2,
            available=True,
            model='F-100'
            
        )

    def test_product_str(self):
        product = Product.objects.first()
        self.assertEqual(str(product), 'Product')

    def test_book_absolute_url_with_200(self):
        product = Product.objects.first()
        self.assertEqual(product.get_absolute_url(), '/single/product')
        response = self.client.get(product.get_absolute_url())
        self.assertEqual(response.status_code, 200)


    


    # def test_name_max_length(self):
    #     category = Category.objects.get(id=1)
    #     max_lenght = category['max_lenght']
    #     self.assertEqual(max_lenght, 200)

    
