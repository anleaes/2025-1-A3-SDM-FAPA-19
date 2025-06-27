from django.db import models
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Conteúdo')
    publication_date = models.DateField('Data de Publicação', auto_now_add=True)

    class Meta:
        verbose_name = 'Artigo de Notícia'
        verbose_name_plural = 'Artigos de Notícias'
        ordering = ['-publication_date']

    def __str__(self):
        return self.title