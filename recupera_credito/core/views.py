from django.http import JsonResponse
from rest_framework import viewsets, filters
from recupera_credito.core.helpers import empresa_to_dict
from recupera_credito.core.helpers import define_donos_de_empresa
from filters.mixins import FiltersMixin
from recupera_credito.core.models import Individuo, Pessoa, Empresa, Bem
from recupera_credito.core.validations import pessoa_query_schema
from recupera_credito.core.serializers import (IndividuoPolymorphicSerializer,
                                               PessoaSerializer,
                                               EmpresaSerializer,
                                               BemSerializer)


class IndividuoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Individuo.objects.all()
    serializer_class = IndividuoPolymorphicSerializer


class PessoaViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['nome', 'cpf']
    filter_mapping = {'nome': 'nome'}
    filter_validation_schema = pessoa_query_schema


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        filtered_data = {key: value
                         for key, value in data.items()
                         if key != 'donos' and key in ['nome', 'cnpj']}
        nova_empresa = Empresa(**filtered_data)
        nova_empresa.save()
        if request.data.get('donos'):
            define_donos_de_empresa(nova_empresa, data['donos'])
        nova_empresa.save()
        return JsonResponse(empresa_to_dict(nova_empresa), status=201)

    def update(self, request, *args, **kwargs):
        empresa = self.get_object()
        if request.data.get('nome'):
            empresa.nome = request.data['nome']
        if request.data.get('cpf'):
            empresa.nome = request.data['cpf']
        if request.data.get('donos'):
            define_donos_de_empresa(empresa, request.data['donos'])
        empresa._prefetched_objects_cache = {}
        empresa.save()
        return JsonResponse(empresa_to_dict(empresa), status=201)


class BemViewSet(viewsets.ModelViewSet):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
