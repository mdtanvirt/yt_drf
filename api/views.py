from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer, OrderSerilizer, OrderItemSerizer
from api.models import Product, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
#####
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFileter

class product_list(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Enable filtering, searching and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFileter

    # Filtering by specific fileds 
    filterset_fileds = ['price', 'stock']

    # searchng text-based filed
    search_fields = ['name', 'description']

    # Ordering filter
    ordering_filter = ['price', 'stock', 'name']

    # Default ordering
    ordering = ['price']

class order_list(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('items__product')
    serializer_class = OrderSerilizer