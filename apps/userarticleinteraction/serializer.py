from .models import UserArticleInteraction
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UserArticleInteractionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserArticleInteraction
        fields = ['id', 'user', 'news_article', 'interaction_type', 'interaction_date']