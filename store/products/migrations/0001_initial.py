# Generated by Django 4.2.6 on 2023-10-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128,
                        unique=True,
                        verbose_name="Имя категории продукта",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=128, unique=True, verbose_name="URl"),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=256, unique=True, verbose_name="товар"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=256, unique=True, verbose_name="URL"),
                ),
                ("description", models.TextField(verbose_name="описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="цена"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=0, verbose_name="количество товаров"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="products_images",
                        verbose_name="картинка",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
    ]