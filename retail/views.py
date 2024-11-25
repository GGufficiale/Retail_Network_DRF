from typing import List

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from retail.models import BaseSupplier
from retail.serializers import BaseSupplierSerializer
from users.permissions import IsOwner


class RetailCreateAPIView(generics.CreateAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     retail = serializer.save()
    #     retail.owner = self.request.user
    #     retail.save()


class RetailListAPIView(generics.ListAPIView):
    serializer_class = BaseSupplierSerializer
    queryset = BaseSupplier.objects.all()
    permission_classes = (IsAuthenticated,)
    # filter_backends: list = [DjangoFilterBackend, ]
    # filter_set_fields: List[str] = ["contact__country", ]

    # def get_queryset(self):
    #     queryset = self.queryset.filter(owner=self.request.user)
    #     return queryset


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


# class RetailPublicListAPIView(generics.ListAPIView):
#     serializer_class = BaseSupplierSerializer
#     queryset = BaseSupplier.objects.filter(is_public=True)
#     permission_classes = (AllowAny,)
