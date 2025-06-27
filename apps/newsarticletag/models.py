from django.db import models
from newsarticle.models import NewsArticle
from tag.models import Tag

# Create your models here.
class NewsArticleTag(models.Model):
    news_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tag de Artigo de Notícia'
        verbose_name_plural = 'Tags de Artigos de Notícias'
        unique_together = ('news_article', 'tag')

    def __str__(self):
        return f"{self.news_article.title} - {self.tag.name}"
