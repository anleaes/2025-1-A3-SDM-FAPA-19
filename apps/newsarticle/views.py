from .models import NewsArticle
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import NewsArticleSerializer, BasicNewsArticleSerializer
from django.db.models import Count, Exists, OuterRef, Q, Value, BooleanField, Case, When, Subquery, CharField, IntegerField

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = BasicNewsArticleSerializer

class RecommendedNewsArticleViewSet(viewsets.ModelViewSet):
    serializer_class = NewsArticleSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = NewsArticle.objects.all().defer('content')

        queryset = queryset.annotate(
            total_likes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='like')),
            total_dislikes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='dislike')),
        )

        if self.request.user.is_authenticated:
            user_interaction_exists = UserArticleInteraction.objects.filter(
                news_article=OuterRef('pk'),
                user=self.request.user
            )

        return queryset