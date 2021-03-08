from recupera_credito.core.models import Individuo


def empresa_to_dict(empresa):
    return {
        'id': empresa.id,
        'nome': empresa.nome,
        'cnpj': empresa.cnpj,
        'donos': [pessoa.id for pessoa in empresa.donos.all()]
    }

def define_donos_de_empresa(empresa, donos_ids):
    for individuo in empresa.donos.all():
        if individuo.id not in donos_ids:
            empresa.donos.remove(individuo)
    for individuo_id in donos_ids:
        try:
            individuo = Individuo.objects.get(id=individuo_id)
            if individuo not in empresa.donos.all():
                empresa.donos.add(individuo)
        except:  # NOQA - Não foi possível importar erro
            ...
