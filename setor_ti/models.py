from django.db import models

# Create your models here.


class CallbacksTeste(models.Model):

    nome = models.TextField(default='')
    processado = models.BooleanField(default=False)

class TokensTeste(models.Model):

    token = models.TextField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)
