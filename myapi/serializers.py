from rest_framework import serializers

from .models import Items, ItemsCategory


class Item_serrializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = (
            'id', 'product_name', 'rating', 'price', 'description', 'color', 'images', 'category', 'sub_category',
            'color_pic')


class ItemCategory_serrializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemsCategory
        fields = ('category',)
