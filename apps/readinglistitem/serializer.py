from .models import ReadingListItem
from rest_framework import serializers

class ReadingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListItem
        fields = '__all__'