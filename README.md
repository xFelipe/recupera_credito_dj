 # API de cadastro de bens e identificação dos donos
 
 porta utilizada: `8000`
 
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
