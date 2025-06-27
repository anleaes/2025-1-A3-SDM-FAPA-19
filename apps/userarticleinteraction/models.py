from django.db import models
from django.contrib.auth.models import User
from newsarticle.models import NewsArticle

# Create your models here.
class UserArticleInteraction(models.Model):
    INTERACTION_CHOICES = [
        ('view', 'Visualização'),
        ('like', 'Curtida'),
        ('dislike', 'Não Curtida'),
        ('share', 'Compartilhamento'),
        ('comment', 'Comentário'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    interaction_type = models.CharField('Tipo de Interação', max_length=20, choices=INTERACTION_CHOICES)
    interaction_date = models.DateField('Data de Interação', auto_now_add=True)

    class Meta:
        verbose_name = 'Interação de Usuário com Artigo'
        verbose_name_plural = 'Interações de Usuário com Artigos'
        ordering = ['-interaction_date']
        unique_together = ('user', 'news_article', 'interaction_type')

    def __str__(self):
        return f"{self.user.username} - {self.interaction_type} - {self.news_article.title}"
