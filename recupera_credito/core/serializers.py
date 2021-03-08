from rest_framework import serializers
from recupera_credito.core import models
from rest_polymorphic.serializers import PolymorphicSerializer


class IndividuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Individuo
        fields = ('id', 'url', 'nome')

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = ['id', 'url', 'nome', 'cpf']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = ['id', 'url', 'nome', 'cnpj', 'donos']

class BemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bem
        fields = ['id', 'url', 'dono', 'descricao', 'valor']

class IndividuoPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.Individuo: IndividuoSerializer,
        models.Pessoa: PessoaSerializer,
        models.Empresa: EmpresaSerializer,
    }
