import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Fornecedor(models.Model):
    razao_social = models.CharField("Razão Social", max_length=200)
    nome_fantasia = models.CharField("Fantasia", max_length=200)
    email_contato = models.EmailField("Email de contato", max_length=200)

    def __str__(self):
        return self.nome_fantasia


class Pergunta(models.Model):
    pergunta = models.CharField("Pergunta", max_length=200)
    data_publicacao = models.DateTimeField("Publicado em:")

    def __str__(self):
        return self.pergunta

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_publicacao <= now


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.resposta
