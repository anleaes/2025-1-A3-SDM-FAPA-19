from .models import NewsArticle
from rest_framework import serializers
from userarticleinteraction.serializer import UserArticleInteractionSerializer
from readinglistitem.serializer import ReadingListItemSerializer
from newsarticletag.models import NewsArticleTag
from newsarticlecategory.models import NewsArticleCategory
from tag.models import Tag
from category.models import Category
from tag.serializer import TagSerializer
from category.serializer import CategorySerializer

class NewsArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_interactions = serializers.SerializerMethodField()
    reading_list_items = serializers.SerializerMethodField()
    total_likes = serializers.IntegerField(read_only=True)
    total_dislikes = serializers.IntegerField(read_only=True)
    tags = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Tag.objects.all(), required=False
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Category.objects.all(), required=False
    )

    def get_user_interactions(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            interactions = obj.userarticleinteraction_set.filter(user=request.user)
            return UserArticleInteractionSerializer(interactions, many=True).data
        return []

    def get_reading_list_items(self, obj):
        reading_list_items = obj.readinglistitem_set.all()
        return ReadingListItemSerializer(reading_list_items, many=True).data

    def get_tags(self, obj):
        return TagSerializer([nat.tag for nat in obj.newsarticletag_set.all()], many=True).data

    def get_categories(self, obj):
        return CategorySerializer([nac.category for nac in obj.newsarticlecategory_set.all()], many=True).data

    class Meta:
        model = NewsArticle
        fields = [
            'id', 'user', 'title', 'content', 'publication_date',
            'user_interactions', 'total_likes', 'total_dislikes', 'reading_list_items',
            'tags', 'categories', 'tag_ids', 'category_ids'
        ]

    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])
        category_ids = validated_data.pop('category_ids', [])
        
        news_article = NewsArticle.objects.create(**validated_data)
        
        for tag in tag_ids:
            NewsArticleTag.objects.create(news_article=news_article, tag=tag)
            
        for category in category_ids:
            NewsArticleCategory.objects.create(news_article=news_article, category=category)
            
        return news_article

    def update(self, instance, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])
        category_ids = validated_data.pop('category_ids', [])

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.save()

        instance.newsarticletag_set.all().delete()
        for tag in tag_ids:
            NewsArticleTag.objects.create(news_article=instance, tag=tag)

        instance.newsarticlecategory_set.all().delete()
        for category in category_ids:
            NewsArticleCategory.objects.create(news_article=instance, category=category)

        return instance

class BasicNewsArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    def get_tags(self, obj):
        return TagSerializer([nat.tag for nat in obj.newsarticletag_set.all()], many=True).data

    def get_categories(self, obj):
        return CategorySerializer([nac.category for nac in obj.newsarticlecategory_set.all()], many=True).data

    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'content', 'publication_date', 'tags', 'categories']