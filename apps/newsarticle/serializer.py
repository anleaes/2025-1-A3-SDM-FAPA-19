from .models import NewsArticle
from rest_framework import serializers
from userarticleinteraction.serializer import UserArticleInteractionSerializer

class NewsArticleSerializer(serializers.ModelSerializer):
    user_interactions = serializers.SerializerMethodField()
    total_likes = serializers.IntegerField(read_only=True)
    total_dislikes = serializers.IntegerField(read_only=True)

    def get_user_interactions(self, obj):
        interactions = obj.userarticleinteraction_set.all()
        return UserArticleInteractionSerializer(interactions, many=True).data

    class Meta:
        model = NewsArticle
        fields = [
            'id', 'title', 'content', 'publication_date',
            'user_interactions', 'total_likes', 'total_dislikes'
        ]
        read_only_fields = ['content']

class BasicNewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'content', 'publication_date']
        read_only_fields = ['content']