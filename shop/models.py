from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    descriptions = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Cart(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    descriptions = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото",)
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

