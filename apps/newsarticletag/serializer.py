from .models import NewsArticleTag
from rest_framework import serializers

class NewsArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticleTag
        fields = '__all__'