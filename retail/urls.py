from django.urls import path


from retail.apps import RetailConfig
from retail.views import RetailListAPIView, RetailCreateAPIView, RetailUpdateAPIView, RetailRetrieveAPIView, \
    RetailDestroyAPIView, RetailPublicListAPIView

app_name = RetailConfig.name


urlpatterns = [
    path('retail/', RetailListAPIView.as_view(), name='retail_list'),
    path('retail/<int:pk>/', RetailRetrieveAPIView.as_view(), name='retail_retrieve'),
    path('retail/create/', RetailCreateAPIView.as_view(), name='retail_create'),
    path('retail/<int:pk>/update/', RetailUpdateAPIView.as_view(), name='retail_update'),
    path('retail/<int:pk>/delete/', RetailDestroyAPIView.as_view(), name='retail_delete'),
    path('public/', RetailPublicListAPIView.as_view(), name='public_list')
]
