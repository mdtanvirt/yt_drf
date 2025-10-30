from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

''''urlpatterns = [
    path('products/', views.product_list.as_view()),
    path('products/<int:pk>', views.product_details.as_view()),
    path('orders/', views.order_list),
]'''

router = DefaultRouter()
router.register('product', views.product_list, basename='product')
router.register('order', views.order_list, basename='order')

urlpatterns = router.urls