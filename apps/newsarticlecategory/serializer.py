from .models import NewsArticleCategory
from rest_framework import serializers

class NewsArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticleCategory
        fields = '__all__'