from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100)
    created_at = models.DateField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Lista de Leitura'
        verbose_name_plural = 'Listas de Leitura'
        ordering = ['-created_at']

    def __str__(self):
        return self.name