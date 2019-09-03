from rest_framework import serializers
from .models import Search


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 'label', 'path', 'favorites', 'image_url', 'directions_url',
                  'ingredients', 'calories')
