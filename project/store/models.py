from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=False,  # Название товароа не должны повторяться
    )
    discription = models.TextField(max_length=255)
    quanity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # Поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',  # все продукты в категории будут доступны через поля products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.discription}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])




class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)




class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.name.title()







