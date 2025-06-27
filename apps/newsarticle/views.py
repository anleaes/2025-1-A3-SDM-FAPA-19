from .models import NewsArticle
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializer import NewsArticleSerializer, BasicNewsArticleSerializer
from django.db.models import Count, Exists, OuterRef, Q, Value, BooleanField, Case, When, Subquery, CharField, IntegerField, Prefetch
from userarticleinteraction.models import UserArticleInteraction
from readinglistitem.models import ReadingListItem
from newsarticletag.models import NewsArticleTag
from newsarticlecategory.models import NewsArticleCategory
from django.contrib.auth.models import User

class PublicNewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = NewsArticle.objects.all().defer('content')
        queryset = queryset.annotate(
            total_likes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='like')),
            total_dislikes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='dislike')),
        )
        return queryset

class UserNewsArticleViewSet(viewsets.ModelViewSet):
    serializer_class = NewsArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = NewsArticle.objects.filter(user=self.request.user).defer('content')
        queryset = queryset.annotate(
            total_likes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='like')),
            total_dislikes=Count('userarticleinteraction', filter=Q(userarticleinteraction__interaction_type='dislike')),
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to access this article.")
        return obj