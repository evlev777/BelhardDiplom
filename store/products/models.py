from django.db import models

from users.models import User

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


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    @classmethod
    def create_or_update(cls, user, product_id):
        baskets = Basket.objects.filter(user=user, product_id=product_id)


        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True

            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_created = False

            return basket, is_created



