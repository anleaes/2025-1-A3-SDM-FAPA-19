from .models import NewsArticleCategory
from rest_framework import viewsets
from .serializer import NewsArticleCategorySerializer

class NewsArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsArticleCategory.objects.all()
    serializer_class = NewsArticleCategorySerializer
