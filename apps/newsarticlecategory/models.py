from django.db import models
from newsarticle.models import NewsArticle
from category.models import Category

# Create your models here.
class NewsArticleCategory(models.Model):
    news_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria de Artigo de Notícia'
        verbose_name_plural = 'Categorias de Artigos de Notícias'
        unique_together = ('news_article', 'category')

    def __str__(self):
        return f"{self.news_article.title} - {self.category.name}"
