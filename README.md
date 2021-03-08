 # API de cadastro de bens e identificação dos donos
 
 ## Como rodar projeto:
  - Via docker-compose: `docker-compose up`
  - Com python local:
    - Preparação de ambiente: `pipenv shell` ou `pip install -r requirements.txt`
    - Execução de migrações: `python manage.py migrate`
    - Inicialização do servidor: `python manage.py runserver`
 porta utilizada: `8000`
 
 ## Documentação
 Rotas:
  - Root da API/documentação: `/api/`
  - Recurso Pessoas:
    - Atributos:
      - nome (String)
      - cpf (String)
    - `/api/pessoas/` [`GET`, `POST`]
      - Aceita o parâmetro de busca, para que seja possível fazer busca por CPF. Exemplo: `/api/pessoas/?search=49258320591`
    - `/api/pessoas/{id}/` [`GET`, `POST`, `PUT`, `DELETE`]
  - Recurso Empresas: 
    - Atributos:
      - nome String
      - cnpj String
      - donos [individuos_ids]
    - `/api/empresas/` [`GET`, `POST`]
    - `/api/empresas/{id}/` [`GET`, `POST`, `PUT`, `DELETE`]
  - Recurso Indivíduo:
    - Engloba Pessoas e Empresas
    - `/api/individuos/` [`GET`]
    - `/api/individuos/{id}/` [`GET`]
  - Recurso Bens:
    - Atributos:
      - descricao String
      - dono individuo_id
      - valor float
    - `/api/bens/` [`GET`, `POST`]
    - `/api/bens/{id}/` [`GET`, `POST`, `PUT`, `DELETE`]
