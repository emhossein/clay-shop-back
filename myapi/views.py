from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Item_serrializer, ItemCategory_serrializer
from .models import Items, ItemsCategory


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.raw('select * from items')
    serializer_class = Item_serrializer


class ItemMensViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.raw('select * from mens_items')
    serializer_class = Item_serrializer


class ItemWomensViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.raw('select * from womens_items')
    serializer_class = Item_serrializer


class ItemCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsCategory.objects.raw('select distinct category from categories where category like "%mens >%"')
    serializer_class = ItemCategory_serrializer
