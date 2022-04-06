from django.forms import ValidationError
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

    def test_max_length(self):
        cat = Category.objects.first()
        max_length = cat._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_book_absolute_url_with_200(self):
        category = Category.objects.first()
        self.assertEqual(category.get_absolute_url(), '/shop/sihofazatroni')
        response = self.client.get(category.get_absolute_url())
        self.assertEqual(response.status_code, 200)


class BrendModelTestCase(TestCase):
    """Тест бренда"""

    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name='brand')

    def test_max_length(self):
        brand = Brand.objects.first()
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_first_name(self):
        brand = Brand.objects.first()
        self.assertEqual(str(brand), 'brand')


class OperatingSystemsTestCase(TestCase):
    """Тест ос"""

    @classmethod
    def setUpTestData(cls):
        OperatingSystems.objects.create(name='ososos')

    def test_max_length(self):
        Os = OperatingSystems.objects.first()
        max_length = Os._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_first_name(self):
        Os = OperatingSystems.objects.first()
        self.assertEqual(str(Os), 'ososos')


class PlatformTestCase(TestCase):
    """Тест платформы"""

    @classmethod
    def setUpTestData(cls):
        Platform.objects.create(name='platform')

    def test_first_name(self):
        plt = Platform.objects.first()
        self.assertEqual(str(plt), 'platform')

    def test_max_lenght(self):
        name = Platform.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

class RamTestCase(TestCase):
    """Тест на пренадлежность поля count к числу"""

    @classmethod
    def setUpTestData(cls):
        Ram.objects.create(count=4)
        
    def test_count(self):
        ram = Ram.objects.values('count').first()
        ram = [i for i in ram.values()]
        self.assertEqual(int(*ram), 4)


# class ProductModelTestCase(TestCase):
#     """Тест продукта"""
    
#     @classmethod
#     def setUpTestData(cls):
#         category = Category.objects.create(name='Категория')
#         brand = Brand.objects.create(name='Opple')
#         os = OperatingSystems.objects.create(name='Ondroid')
#         platform = Platform.objects.create(name='Ondro')
#         ram = Ram.objects.create(count=1)
#         product = Product.objects.create(
#             category=category,
#             name='Product',
#             slug='product',
#             description='product123',
#             price=1010,
#             stock=2,
#             available=True,
#             model='F-100'
            
#         )


#     def test_product_str(self):
#         product = Product.objects.first()
#         self.assertEqual(str(product), 'Product')

#     def test_book_absolute_url_with_200(self):
#         product = Product.objects.first()
#         self.assertEqual(product.get_absolute_url(), '/single/product')
#         response = self.client.get(product.get_absolute_url())
#         self.assertEqual(response.status_code, 200)


    # def test_name_max_length(self):
        #     category = Category.objects.get(id=1)
        #     max_lenght = category['max_lenght']
        #     self.assertEqual(max_lenght, 200)


# class ProductShotsTestCase(TestCase):
    

#     @classmethod
#     def setUpTestData(cls):
#         ProductShots.objects.create(
#             title='Заголовок1',
#             description='Описание1',
#             image='image.img',
#         )

    
class RatingStarTestCase(TestCase):


    @classmethod
    def setUpTestData(cls):
        RatingStar.objects.create(value=4)

    def test_validator(self):
        star = RatingStar(value=6)
        with self.assertRaises(ValidationError):
            star.full_clean()#вызов валидатора и попытка сохранить
            star.save()


# class RatingTestCase(TestCase):

    
#     @classmethod
#     def setUpTestData(cls):
#         Rating.objects.create(
#             ip='12.1.1.8080',
#             star=RatingStar.objects.create(value=1),
#             product=Product.objects.create(
#                 name='prod'
#             )
#         )

#     def test_length_ip(self):
#         ip = Rating.objects.first()
#         max_length = ip._meta.get_field('ip').max_length
#         self.assertEqual(max_length, 15)


