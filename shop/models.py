from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User



class Category(models.Model):
    """Категории"""

    name = models.CharField('Название категории', max_length=200, db_index=True)
    slug = models.SlugField('URL', max_length=200, db_index=True, unique=True)
    image = models.ImageField(
        'Изображение', upload_to='category/%Y/%m/%d', blank=True
    )

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Бренд"""


    name = models.CharField('Название', max_length=100)
    image = models.ImageField(
        'Изображение', upload_to='brand/%Y/%m/%d', blank=True
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name


class OperatingSystems(models.Model):
    """Операционная система"""

    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class Platform(models.Model):
    """Платформа"""

    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class Ram(models.Model):
    """Кол-во ядер"""

    count = models.IntegerField('Количество ядер')
    
    def __str__(self) -> str:
        if self.count == 1:
            return f'{self.count} ядро'
        if self.count == 2 or self.count == 4:
            return f'{self.count} ядра'
        return f'{self.count} ядер'


class Product(models.Model):
    """Продукт"""

    category = models.ForeignKey(
        Category, related_name='products', 
        on_delete=models.CASCADE, verbose_name='Категория'
    )
    name = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField('Юрл', max_length=200, db_index=True)
    image = models.ImageField(
        'Изображение', upload_to='products/%Y/%m/%d', blank=True
    )
    description = models.TextField('Описание продукта', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Остаток продукта')
    available = models.BooleanField('Наличие в ассортименте', default=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)
    model = models.CharField('Модель', max_length=100, db_index=True)
    manufacturer = models.ForeignKey(
        Brand, max_length=100, 
        default=None, 
        verbose_name='Производитель', 
        on_delete=models.SET_NULL, 
        null=True
    )
    os = models.ManyToManyField(
        OperatingSystems, verbose_name='Операционная система', blank=True
    )
    platform = models.ManyToManyField(
        Platform, verbose_name='Платформа', blank=True
    )
    ram = models.ManyToManyField(Ram, verbose_name='Озу', blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class ProductShots(models.Model):
    """Доп фото к продукту"""

    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots')
    product = models.ForeignKey(
        Product, verbose_name='Продукт', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительное фото'


class RatingStar(models.Model):
    """Звезда рейтинга"""

    value = models.PositiveSmallIntegerField(
        'Значение', 
        default=0, 
        validators=[MaxValueValidator(5, 'Кол-во звезд не больше 5')]
    )

    def __str__(self) -> str:
        if self.value == 1:
            return f'{self.value} звезда'
        if self.value == 5 or self.value == 0:
            return f'{self.value} звезд'
        return f'{self.value} звезды'

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'


class Rating(models.Model):
    """Рейтинг"""

    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name='Звезда'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт'
    )

    def __str__(self) -> str:
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', 
        on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(
        Product, verbose_name='продукт', on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(
        User, blank=True, null=True, 
        on_delete=models.PROTECT, verbose_name='Автор комментария'
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']
