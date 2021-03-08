import six
from filters.schema import base_query_params_schema
from filters.validations import IntegerLike


pessoa_query_schema = base_query_params_schema.extend(
    {
        'nome': six.text_type,
        'cpf': six.text_type,
    }
)