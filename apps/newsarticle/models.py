from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Conteúdo')
    publication_date = models.DateField('Data de Publicação', auto_now_add=True)

    class Meta:
        verbose_name = 'Artigo de Notícia'
        verbose_name_plural = 'Artigos de Notícias'
        ordering = ['-publication_date']

    def __str__(self):
        return self.title
