from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Имя категории продукта'
    )

    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URl'
    )

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        unique=True,
        verbose_name='товар'
    )

    slug = models.SlugField(
        max_length=256,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='описание'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name='цена'
    )

    quantity = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='количество товаров'
    )

    image = models.ImageField(
        upload_to='products_images',
        null=True,
        blank=True,
        verbose_name='картинка'
    )

    category = models.ForeignKey(
        to='ProductCategory',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'