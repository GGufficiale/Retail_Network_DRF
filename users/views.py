from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer


# class UserViewSet(ViewSet):
#     """
#     ViewSet для работы с моделью User
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

# class MyTokenObtainPairView(TokenObtainPairView):
#     """
#     API для получения токенов JWT
#     """
#     serializer_class = MyTokenObtainPairSerializer
