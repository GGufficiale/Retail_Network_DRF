from datetime import datetime
from typing import List

from django.db import models

NULLABLE = {'blank': True, 'null': True}  # форма, если параметр необязателен


class BaseSupplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название',
                            help_text="Введите название поставщика")
    supplier = models.ForeignKey('self', **NULLABLE, default=None, on_delete=models.SET_DEFAULT,
                                 verbose_name='Поставщик')
    level = models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], verbose_name='Уровень в сети')
    debt = models.DecimalField(verbose_name='Долг перед поставщиком', help_text='Укажите долг перед поставщиком',
                               max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(**NULLABLE, verbose_name='Дата создания записи в БД', auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = False
        verbose_name: str = 'сетевой элемент'
        verbose_name_plural: str = 'сетевые элементы'
        ordering: List[str] = ['level']

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_of_creation = datetime.now()
        return super().save(*args, **kwargs)


class Contacts(models.Model):
    base_supplier = models.OneToOneField(BaseSupplier, on_delete=models.CASCADE, **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='Email', help_text="Введите имэйл")
    country = models.CharField(max_length=50, verbose_name="Страна", **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="Город", **NULLABLE)
    street = models.CharField(max_length=50, verbose_name="Улица", **NULLABLE)
    house_number = models.IntegerField(verbose_name="№ дома", **NULLABLE)

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.house_number}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта', help_text="Введите продукт")
    description = models.CharField(max_length=1000, verbose_name='Описание', help_text="Введите описание продукта",
                                   **NULLABLE)
    model = models.CharField(max_length=1000, verbose_name='Модель', help_text="Введите модель продукта", **NULLABLE)
    photo = models.ImageField(upload_to='retail/photo', verbose_name="Фото продукта", **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', help_text="Введите цену продукта")
    manufactured_at = models.DateField(**NULLABLE, verbose_name='Дата выхода продукта на рынок',
                                       help_text="Введите дату выхода продукта на рынок")
    owner = models.ForeignKey(BaseSupplier, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.description}. Модель:{self.model}. Цена: {self.price}. Поставщик: {self.owner}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description', 'model', 'price']
