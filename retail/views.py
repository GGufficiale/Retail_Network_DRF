from typing import List

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from retail.models import BaseSupplier
from retail.serializers import BaseSupplierSerializer
from users.permissions import IsOwner


class RetailListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if country := self.request.query_params.get('country'):
            return BaseSupplier.objects.filter(contacts_country__icontains=country)
        return BaseSupplier.objects.all()


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class RetailUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class RetailDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
