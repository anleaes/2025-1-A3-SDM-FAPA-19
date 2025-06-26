from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField('Nome', max_length=50)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering =['id']

    def __str__(self):
        return self.name