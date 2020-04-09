from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feito'),
    )

    title = models.CharField('Titulo', max_length=255)
    description = models.TextField('Descrição')
    status = models.CharField(max_length=5, choices=STATUS,)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.title
