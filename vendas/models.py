from django.db import models
from reciclagem.models import Produto, Categoria, Imagem

class Venda(models.Model):

    nome = models.CharField(max_length=40)
    quantidade = models.FloatField()
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    total = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    
def Multiplicacao(self, total):
    return self.preco_venda * self.quantidade



