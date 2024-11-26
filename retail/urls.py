from django.urls import path


from retail.apps import RetailConfig
from retail.views import RetailListCreateAPIView, RetailUpdateAPIView, RetailRetrieveAPIView, RetailDestroyAPIView

app_name = RetailConfig.name


urlpatterns = [
    path('retail/', RetailListCreateAPIView.as_view(), name='retail_list'),
    path('retail/<int:pk>/', RetailRetrieveAPIView.as_view(), name='retail_retrieve'),
    path('retail/<int:pk>/update/', RetailUpdateAPIView.as_view(), name='retail_update'),
    path('retail/<int:pk>/delete/', RetailDestroyAPIView.as_view(), name='retail_delete'),
]
