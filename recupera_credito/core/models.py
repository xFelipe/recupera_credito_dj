from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
class Individuo(PolymorphicModel):
    nome = models.CharField(max_length=255)

class Pessoa(Individuo):
    cpf = models.CharField(max_length=11, null=False, unique=True)

class Empresa(Individuo):
    cnpj = models.CharField(max_length=14, null=False, unique=True)
    donos = models.ManyToManyField(Individuo, related_name='donos')

class Bem(models.Model):
    dono = models.ForeignKey(Individuo, on_delete=models.CASCADE, null=False)
    descricao = models.TextField(null=False)
    valor = models.FloatField()  # Adicionar validador de valor mínimo(0)