from .models import ReadingList
from rest_framework import serializers

class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = '__all__'