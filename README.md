## Galeria de Artes Online - Backend

Este repositório contém a API (Backend) do projeto de Galeria de Artes, responsável por conectar o banco de dados e o armazenamento de imagens com a aplicação web.

###  Aluno
* **Nome:** João Gois de Otoni - 202303038305
* **Disciplina:** Projeto Cloud


### Tecnologias 
* **Linguagem:** Python 3.13
* **Cloud Provider:** Microsoft Azure
* **Serverless:** Azure Functions (HTTP Trigger)
* **Banco de Dados:** Azure Database for PostgreSQL
* **Armazenamento de Imagens:** Azure Blob Storage
* **CI/CD:** GitHub Actions

### Funcionalidades
* **Rota `/api/obter_obras`:** Consulta o banco de dados PostgreSQL e retorna uma lista JSON com as obras de arte, incluindo link direto para a imagem no Blob Storage.
* **Conexão Segura:** Utiliza variáveis de ambiente para credenciais sensíveis.
* **CORS Habilitado:** Permite requisições de origens externas (Frontend).

