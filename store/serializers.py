from . models import ItemModel
from rest_framework import serializers


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        lookup_field = 'slug'
