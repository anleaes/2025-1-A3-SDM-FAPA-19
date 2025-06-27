from .models import NewsArticleTag
from rest_framework import viewsets
from .serializer import NewsArticleTagSerializer

class NewsArticleTagViewSet(viewsets.ModelViewSet):
    queryset = NewsArticleTag.objects.all()
    serializer_class = NewsArticleTagSerializer
