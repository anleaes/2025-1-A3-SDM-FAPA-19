from django.db import models
from readinglist.models import ReadingList
from newsarticle.models import NewsArticle

# Create your models here.
class ReadingListItem(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    news_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    added_at = models.DateField('Adicionado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Item da Lista de Leitura'
        verbose_name_plural = 'Itens da Lista de Leitura'
        ordering = ['-added_at']
        unique_together = ('reading_list', 'news_article')

    def __str__(self):
        return f"{self.news_article.title} in {self.reading_list.name}"
