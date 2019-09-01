from rest_framework import serializers
from .models import Search


class SearchSerializers(serializers.ModelSerializers):
    class Meta:
        model = Search
        fields = ('id', 'label', 'favorites', 'image_url', 'directions_url',
                  'ingredients', 'calories', 'total time')
