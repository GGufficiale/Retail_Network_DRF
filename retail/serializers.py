from typing import Tuple, Dict, List

from rest_framework import serializers

from retail.models import BaseSupplier, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class BaseSupplierSerializer(serializers.ModelSerializer):
    # supplier = serializers.SlugRelatedField(required=False, queryset=NetElement.objects.all(), slug_field="name")
    # contact = ContactsSerializer(required=False)

    class Meta:
        model = BaseSupplier
        read_only_fields: Tuple[str, ...] = ("id", "debt", "created_at", "level")
        fields = '__all__'

    # def is_valid(self, *, raise_exception=False):
    #
    #     """
    #     Функция для проверки валидности аргументов объекта сети
    #     """
    #
    #     self._contact = self.initial_data.pop("contact", {})
    #     if "supplier" in self.initial_data:
    #         self.initial_data["level"] = level_detection(self.initial_data)
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self):
    #
    #     """
    #     Функция проверки и сохранения значений, содержащихся в аргументах контакта объекта сети
    #     """
    #
    #     super().save()
    #
    #     if self._contact != {}:
    #         self.instance.contact = self.update(self.instance.contact, self._contact)
    #
    #     return self.instance


#
#
# class BaseSupplierCreateSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор для создания модели сетевого элемента
#     """
#
#     supplier = serializers.SlugRelatedField(required=False, queryset=BaseSupplier.objects.all(), slug_field="name")
#     contact = ContactsSerializer(required=False)
#
#     class Meta:
#         model = BaseSupplier
#         read_only_fields: Tuple[str, ...] = ("id", "debt", "date_of_creation")
#         fields: str = "__all__"
#
#     def is_valid(self, *, raise_exception=False):
#         """
#         Проверка валидности сетевого элемента с контактом.
#         """
#
#         self._contact: Dict[str, str] = self.initial_data.pop("contact", {})
#         self.initial_data["level"] = level_detection(self.initial_data)
#         return super().is_valid(raise_exception=raise_exception)
#
#     def create(self, validated_data: dict) -> BaseSupplier:
#         """
#         Создание модели сетевого элемента с контактом
#         """
#
#         net_element: BaseSupplier = BaseSupplier.objects.create(**validated_data)
#         net_element.save()
#
#         contact: Contacts = Contacts.objects.create(
#             base_class=net_element,
#             email=self._contact.get("email", None),
#             country=self._contact.get("country", None),
#             city=self._contact.get("city", None),
#             street=self._contact.get("street", None),
#             house_number=self._contact.get("house_number", None)
#         )
#         contact.save()
#
#         return net_element
#
#
# class BaseSupplierListSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор для списка моделей сетевых элементов
#     """
#
#     supplier = serializers.SlugRelatedField(queryset=BaseSupplier.objects.all(), slug_field="name")
#     contact = ContactsSerializer()
#
#     class Meta:
#         model = BaseSupplier
#         fields: List[str] = ["id", "name", "level", "supplier", "debt", "contact"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# def level_detection(kwargs: dict) -> int:
#     """
#     Функция определения иерархического уровня элемента сети
#     """
#
#     level: int = 0
#     if kwargs["supplier"] is None:
#         return level
#
#     supplier: BaseSupplier = BaseSupplier.objects.get(name=kwargs["supplier"])
#
#     for i in range(2):
#         level += 1
#         if supplier.supplier is None:
#             return level
#         supplier = supplier.supplier
#
#     raise Exception("Некорректное значение в иерархической системе")
