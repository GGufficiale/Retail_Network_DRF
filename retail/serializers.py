from rest_framework import serializers

from retail.models import BaseSupplier, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class BaseSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSupplier
        read_only_fields = ("id", "created_at",)
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
